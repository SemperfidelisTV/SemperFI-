'''
Muchshare urlresolver plugin
Copyright (C) 2013 Vinnydude

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

from t0mm0.common.net import Net
from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin
import re, urllib2
from urlresolver import common

class MuchshareResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "muchshare"
    domains = ["muchshare.net"]

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)
        self.net = Net()

    def get_media_url(self, host, media_id):
        url = self.get_url(host, media_id)
        html = self.net.http_GET(url).content

        err = re.compile('<p class="err">(.+?)<br>').findall(html)
        if err:
            raise UrlResolver.ResolverError(str(err))

        data = {}
        r = re.findall(r'type="(?:hidden|submit)?" name="(.+?)"\s* value="?(.+?)">', html)
        for name, value in r:
            data[name] = value
        data.update({'down_direct': 1})
        
        common.addon.show_countdown(45, title='Muchshare', text='Loading Video...')
        html = self.net.http_POST(url, data).content
        r = re.search("(?:.+var file_link = \'|.+\<a id=\"lnk_download\" href=\")(.+?)(?:\'|\"\>)", html).group(1)
        r = urllib2.unquote(r)
        return r
 
    def get_url(self, host, media_id):
        return 'http://muchshare.net/%s' % media_id
        
    def get_host_and_id(self, url):
        r = re.search('//(.+?)/([0-9a-zA-Z]+)',url)
        if r:
            return r.groups()
        else:
            return False
        return('host', 'media_id')

    def valid_url(self, url, host):
        return (re.match('http://(www.)?muchshare.net/' +
                         '[0-9A-Za-z]+', url) or
                         'muchshare' in host)

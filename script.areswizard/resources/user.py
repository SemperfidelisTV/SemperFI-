exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MjkgNDEsIDZiLCBkYywgMTAsIGIzLCA0MwoyOSAxOCxiNiwgYjUsIGIyCjI5IGFmLCBjMiwgM2YsIGIzLjllCjljIDQxIDI5IDQ5IDg2IDk3CjI5IDFkLCBiYgo5YyA5OCAyOSBhNgoyOSAxMwoKCjgxPSAnYjEuMWMnCjgyID0gNmIuYzEoODEpCjZmID0gNDEuNDkoODIuODcoJ2E5JykpCjFhID0gYjMuOWUuYzYoNmYsICdhNCcpCgoKMzAgMTkKMTkgPSAnMmMuZDInCjFmID0gImJhIgoKMzAgZGEKZGEgPSAxMC4xNSgzNCg0My4zN1sxXSksICdkYScpCgozMCAxNAoxNCA9IDEwLjE1KDM0KDQzLjM3WzFdKSwgJzE0JykKMzAgMWIKMWIgPSAxMC4xNSgzNCg0My4zN1sxXSksICcxYicpCjMwIDgKOCA9IDEwLjE1KDM0KDQzLjM3WzFdKSwgJzgnKQozMCA4ZQo4ZSA9IDEwLjE1KDM0KDQzLjM3WzFdKSwgJzhlJykKCgoKCgoKCgoKNTAgYjAoMWQpOgoJCgk3NyA9IGRjLjYoKQoJNzcuMmUoIjFkIiwgMWQsICIiLCIiKQoJCgo1MCAyZCg4YSwgMzUsIDQ2LCA2YT1hMik6CgkyNSA2YToKCSAgIGI3OiBhYSA9IGI1Ljg4KCIoP2RlKSIgKyAzNSArICIoW1xhY1xlMl0rPykiICsgNDYsIDhhKS45MygxKQoJICAgOGI6IGFhID0gJycKCTUyOgoJICAgYjc6IGFhID0gYjUuODgoIig/ZGUpKCIgKyAzNSArICJbXGFjXGUyXSs/IiArIDQ2ICsgIikiLCA4YSkuOTMoMSkKCSAgIDhiOiBhYSA9ICcnCgk5YSBhYQoKCjUwIDdlKDFkKToKCgk3MCA9ICJlNCIKCTI1IDcwIGRmIDFkOgoJCTdkID0gMWQuOGMoJ10nKQoJCTQ4ID0gMWRbN2QrMTpdCgkJNzUgPSA0OC44YygnWycpCgkJMWQgPSA0OFs6NzVdCgkJOWEgMWQKCgkJCjUwIDZlKDI2LCBlNSk6CgoJOTEoKQoKCQkJCgkJCgk5ID0gNDEuMzkoIiIsICIzYiA1YiA3MyAxNCBhYiIpCgk5LjNlKCkKCTIyID0gOS40MigpCgkKCTkgPSA0MS4zOSgiIiwgIjNiIDViIGEgMjQgZGIgNzEgODQgKGNmIGJlIGI4IGNkIGEgZGEpIikKCTkuM2UoKQoJYTEgPSA5LjQyKCkKCQoJOSA9IDQxLjM5KCIiLCAiM2IgNWIgNzMgMTYiKQoJOS44MChhMikKCTkuM2UoKQoJMjEgPSA5LjQyKCkKCQoJCgkKCQoJCgkjIDE3ID0geydlNSc6IGU1fQoJCgkjIDUxIDYyKDFhLCAnZDQnKSA4NiBmOgoJCSMgM2YuODkoMTcsIGYpCgkKCSMgZi43YgoJCgkKCTgyLmQ2KCJlNSIsIGU1KQoJODIuZDYoImRhIiwgYTEpCgkjIDgyLmQ2KCIxNCIsIDIyKQoJCgoJCgkJCglkID0gJzVlOi8vN2EuNzguNDcuN2MvfjFjLycrMTkrJz8zYz02ZSY1Yz0nK2ExKycmY2I9JysyMSsnJjE0PScrMjIrJyZlNT0nK2U1KycmYzU9JytjNSsnJmI0PScrYjQrJyY5ZD0nKzlkICsgJyYyNj0nICsgMjYgKyAnJjVkPScgKyAxMy4xMy42YygpLjJhKCclYWMnKQoJCgkzNiA9IGQuNDAgKCIgIiwgIiUyMCIpCgkKCTI1IDggPT0gIjI4IjoKCQljICdAMmM6IDU2IGQ6ICcgKyAyZigzNikKCQoJCgkyNyA9IDE4LjMxKDM2KQoJMjcuMjMoJzYxLTRlJywgMWYpCgkxMiA9IDE4LjMzKDI3KQoJZDkgPSAxMi42NCgpCgoJCQoJMjUgOCA9PSAiMjgiOgoJCWMgJ0AyYzogNTYgNTU6ICcgKyAyZihkOSkKCQoJIyA1MSA2MigxYSwgJ2FhJywwKSA4NiBmOgoJCSMgMTcgPSAzZi45ZihmKQoKCSMgZTUgPSAxN1snZTUnXQoJIyMgZGEgPSAxN1snZGEnXQoJIyMgMTYgPSAxN1snMTYnXQoJIyMgMTQgPSAxN1snMTQnXQoKCQoJCgliID0gImIiCgk1MyA9IGQ5LjhjKGIpCgkKCTI1IDUzIDw+IC0xOgoJCQoJCTI0ID0gMmQoZDksICdiOicsICcvJykKCQk0ZiA9IDJkKGQ5LCAnISEnLCAnISEnKQoJCQoJCQoJCTc3ID0gZGMuNigpCgkJNzcuMmUoIjhkIGEzIiwgIjYwIGM5IGM0IGUxIGE3IisyNCwgIiIsIiIpCgkJODIuZDYoIjFiIiwgIjkyIikKCQkKCQkKCQkKCQkxNyA9IHsnZTUnOiBlNSwgJzE0JzogJ2InfQoJCgkJNTEgNjIoMWEsICdkNCcpIDg2IGY6CgkJCTNmLjg5KDE3LCBmKQoJCQoJCWYuN2IKCQkKCQkKCQk4Mi5kNigiZTUiLCBlNSkKCQk4Mi5kNigiZGEiLCBhMSkKCQkjIDgyLmQ2KCIxNiIsIDRmKQoJCSMgODIuZDYoIjE0IiwgImIiKQoJCQoJCQoJCTlhIChiKQoJCgkKCQoJMjUgZDkgPT0gIjk0IjoKCQoJCgkJODIuZDYoIjFiIiwgIjY1IikKCQk4Mi5kNigiZGEiLCBhMSkKCQkjIDgyLmQ2KCIxNiIsIDIxKQoJCSMgODIuZDYoIjE0IiwgMjIpCgkKCQk3NyA9IGRjLjYoKQoJCTc3LjJlKCIzYiA4ZiA3MyAxNCIsICI4MyAxNCA0NCBjNyA1MSBlMCA2MyBhNS4gKGRkIGQzIGMzIGEgYWUgZTMgYTggZDAgY2EgYWQuLiBkMSdlNiBiYyBkMCA4ZiBjOCBiOSBkNykiLCAiIiwiIikKCQkKCQk3NCA9IHsnZGEnOiBhMSwgJzE2JzogMjEsICcxNCc6IDIyfQoJCQoJCTVmID0gM2YuYmYoNzQpCgkJCgkJCgkJOWEgKDVmKQoJCQoJCQoJCQoJMjUgZDkgPT0gIjZkIjoKCQoJCQoJCQoJCTE3ID0geydlNSc6IGU1fQoJCgkJNTEgNjIoMWEsICdkNCcpIDg2IGY6CgkJCTNmLjg5KDE3LCBmKQoJCQoJCWYuN2IKCQkKCQkKCQk4Mi5kNigiZTUiLCBlNSkKCQk4Mi5kNigiZGEiLCAiIikKCQkjIDgyLmQ2KCIxNCIsICIiKQoJCQoJCQoJCTc3ID0gZGMuNigpCgkJNzcuMmUoIjY3IDE2IiwgIjY3IDE2IiwgIiIsIiIpCgkJCgkJCgkJOWEgKGQ5KQkKCQkKCQkJCgk1MjoKCQkKCQk3NyA9IGRjLjYoKQoJCTc3LjJlKCI0ZCwgNGMgNDQgYSAzMiIsICI4MyA0YiAyYjogXDliXDliICIgKyBkOSwgIiIsIiIpCgkJMjUgOCA9PSAiMjgiOgoJCQljICdAMmM6IGQ6ICcgKyAyZigzNikKCQkKCQk5YSAoZDkpCgkJCgkJCgoJCQo1MCAzOChkYSwgMjYsIGU1KToKCgoKCTkgPSA0MS4zOSgiIiwgIjNiIDViIDczIDYzIGE1IChkOCBhMCkiKQoJOS4zZSgpCgkzZCA9IDkuNDIoKQoJCgk1MSA2MigxYSwgJ2FhJywwKSA4NiBmOgoJCTE3ID0gM2YuOWYoZikKCgllNSA9IDE3WydlNSddCgkKCSMgZGEgPSAxMC4xNSgzNCg0My4zN1sxXSksICdkYScpCgkjIDE2ID0gMTAuMTUoMzQoNDMuMzdbMV0pLCAnMTYnKQoJIyAxNCA9IDEwLjE1KDM0KDQzLjM3WzFdKSwgJzE0JykKCgoJCglkID0gJzVlOi8vN2EuNzguNDcuN2MvfjFjLycrMTkrJz8zYz0zOCY1Yz0nK2RhKycmMjY9JysyNisnJmU1PScrZTUrJyY3Zj0nKzNkICsgJyY1ZD0nICsgMTMuMTMuNmMoKS4yYSgnJWFjJykKCQoJMjUgOCA9PSAiMjgiOgoJCWMgJ0AyYzogMzggZCA9ICcgKyAyZihkKQoJCgkyNyA9IDE4LjMxKGQpCgkyNy4yMygnNjEtNGUnLCAxZikKCTEyID0gMTguMzMoMjcpCglkOSA9IDEyLjY0KCkKCQoJCgkyNSBkOSA9PSAiOTkiOgoJCgkJNzcgPSBkYy42KCkKCQk3Ny4yZSgiNTQiLCAiNjAgODQgYzQgNmMgOTAuLiBjYyBkNSBjMC4uIiwgIiIsIiIpCgkJCgkJOWEgKGQ5KQoJCQoJNTI6CgkJCgkJNzcgPSBkYy42KCkKCQk3Ny4yZSgiNGQsIDRjIDQ0IGEgMzIiLCAiODMgNGIgMmIiLCAiIiwiIikKCQkKCQkKCQkyNSA4ID09ICIyOCI6CgkJCWMgJ0AyYzogMzggMTIgPSAnICsgMmYoZDkpCgkJCWMgJ0AyYzogZDogJyArIDJmKGQpCgkJCgkJCgkJOWEgKGQ5KQoJCQoJCgkKCQo1MCA2NihkYSwgMjQsIDI2LCBlNSk6CgoKCTExID0gWyIxIiwiMiIsIjMiLCI0IiwiNSJdCgkKCWUgPSBkYy42KCkuNjgoIjk2IDg1IDc5PyIsIDExKQoJCgkjIDc3ID0gZGMuNigpCgkjIDc3LjJlKCI1NSIsIDExW2VdLCAiIiwiIikKCQoJCgkxZSA9IDM0KDExW2VdKQoJCgkKCWQgPSAnNWU6Ly83YS43OC40Ny43Yy9+MWMvJysxOSsnPzNjPTY2JjVjPScrZGErJyYyNj0nKzI2KycmMjQ9JysyNCsnJmU1PScrZTUrJyYxZT0nKzJmKDFlKSArICcmNWQ9JyArIDEzLjEzLjZjKCkuMmEoJyVhYycpCgkKCTI1IDggPT0gIjI4IjoKCQljICdANGEgLS0+JwoJCWMgJyAnCgkJYyBkCgkKCWQgPSBkLjQwICgiICIsICIlMjAiKQoJCgkyNSA4ID09ICIyOCI6CgkJYyAnQDRhIC0tPicKCQljICcgJwoJCWMgZAoJCgkjYyBkCgkKCTI3ID0gMTguMzEoZCkKCTI3LjIzKCc2MS00ZScsIDFmKQoJMTIgPSAxOC4zMygyNykKCTcgPSAxMi42NCgpCgkKCTI1IDggPT0gIjI4IjoKCQljICdANzIgLS0+JwoJCWMgJyAnCgkJYyA3CgkKCgkyNSA3ID09ICI1NyI6CgoJCTc3ID0gZGMuNigpCgkJNzcuMmUoIjU0IiwgIjYwIDExIDQ0IDU4IiwgIiIsIiIpCgkJCgkJOWEKCQkKCQoJMjUgNyA9PSAiNDUiOgoKCQk3NyA9IGRjLjYoKQoJCTc3LjJlKCI1OSAzYSIsICI5NSA1YSAzYSA3MSA4MiIsICIiLCIiKQoJCQoJCTlhCgkJCgk1MjoKCQkKCQk3NyA9IGRjLjYoKQoJCTc3LjJlKCI0ZCwgNGMgNDQgYSAzMiIsICI4MyA0YiAyYjogXDliXDliIC0iICsgNywgIiIsIiIpCgkJMjUgOCA9PSAiMjgiOgoJCQljICdAMmM6IGQ6ICcgKyAyZihkKQoJCQoJCTlhCgkKCQoKCQoJCjUwIDY5KGRhLCAyNCwgMjYsIGU1KToKCgoJCQoJCgkxMSA9IFsiMSIsIjIiLCIzIiwiNCIsIjUiXQoJCgllID0gZGMuNigpLjY4KCI5NiA4NSA3OT8iLCAxMSkKCQoJIyA3NyA9IGRjLjYoKQoJIyA3Ny4yZSgiNTUiLCAxMVtlXSwgIiIsIiIpCgkKCQoJMWUgPSAzNCgxMVtlXSkKCQoJCglkID0gJzVlOi8vN2EuNzguNDcuN2MvfjFjLycrMTkrJz8zYz02OSY1Yz0nK2RhKycmMjY9JysyNisnJjI0PScrMjQrJyZlNT0nK2U1KycmMWU9JysyZigxZSkgKyAnJjVkPScgKyAxMy4xMy42YygpLjJhKCclYWMnKQoJCglkID0gZC40MCAoIiAiLCAiJTIwIikKCQkKCgkKCTI3ID0gMTguMzEoZCkKCTI3LjIzKCc2MS00ZScsIDFmKQoJMTIgPSAxOC4zMygyNykKCTcgPSAxMi42NCgpCgkKCgkyNSA3ID09ICI1NyI6CgoJCTc3ID0gZGMuNigpCgkJNzcuMmUoIjU0IiwgIjYwIDExIDQ0IDU4IiwgIiIsIiIpCgkJCgkJOWEKCQkKCQoJMjUgNyA9PSAiNDUiOgoKCQk3NyA9IGRjLjYoKQoJCTc3LjJlKCI1OSAzYSIsICI5NSA1YSAzYSA3MSBiZCIsICIiLCIiKQoJCQoJCTlhCgkJCgk1MjoKCQkKCQk3NyA9IGRjLjYoKQoJCTc3LjJlKCI0ZCwgNGMgNDQgYSAzMiIsICI4MyA0YiAyYjogXDliXDliIC0iICsgNywgIiIsIiIpCgkJMjUgOCA9PSAiMjgiOgoJCQljICdAMmM6IGQ6ICcgKyAyZihkKQoJCQoJCTlhCgkKCQkKCgoJCjUwIDc2KGRhLCAyNCwgMjYsIGU1KToKCgoKCQkKCQoJMTEgPSBbIjEiLCIyIiwiMyIsIjQiLCI1Il0KCQoJZSA9IGRjLjYoKS42OCgiOTYgODUgNzk/IiwgMTEpCgkKCSMgNzcgPSBkYy42KCkKCSMgNzcuMmUoIjU1IiwgMTFbZV0sICIiLCIiKQoJCgkKCTFlID0gMzQoMTFbZV0pCgkKCQoJZCA9ICc1ZTovLzdhLjc4LjQ3LjdjL34xYy8nKzE5Kyc/M2M9NzYmNWM9JytkYSsnJjI2PScrMjYrJyYyND0nKzI0KycmZTU9JytlNSsnJjFlPScrMmYoMWUpICsgJyY1ZD0nICsgMTMuMTMuNmMoKS4yYSgnJWFjJykKCQoJZCA9IGQuNDAgKCIgIiwgIiUyMCIpCgkKCTI3ID0gMTguMzEoZCkKCTI3LjIzKCc2MS00ZScsIDFmKQoJMTIgPSAxOC4zMygyNykKCTcgPSAxMi42NCgpCgkKCgkyNSA3ID09ICI1NyI6CgoJCTc3ID0gZGMuNigpCgkJNzcuMmUoIjU0IiwgIjYwIDExIDQ0IDU4IiwgIiIsIiIpCgkJCgkJOWEKCQkKCQoJMjUgNyA9PSAiNDUiOgoKCQk3NyA9IGRjLjYoKQoJCTc3LjJlKCI1OSAzYSIsICI5NSA1YSAzYSA3MSBjZSIsICIiLCIiKQoJCQoJCTlhCgkJCgk1MjoKCQkKCQk3NyA9IGRjLjYoKQoJCTc3LjJlKCI0ZCwgNGMgNDQgYSAzMiIsICI4MyA0YiAyYjogXDliXDliIC0iICsgNywgIiIsIiIpCgkJMjUgOCA9PSAiMjgiOgoJCQljICdAMmM6IGQ6ICcgKyAyZihkKQoJCQoJCTlhCgkKCQoJCQoKCQo=")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|4|5|Dialog|rateresult|debuglog|keyboard|a|staff_override|print|url|userChoice|f|xbmcplugin|rating|response|datetime|email|getSetting|password|config|urllib2|basephpfile|settingsfile|accountstatus|areswizard|string|points|aresagent|20|passwordinput|emailinput|add_header|name|if|mac|req|true|import|strftime|occurred|ares|regex_from_to|ok|str|global|Request|problem|urlopen|int|from_string|nospaces|argv|activate|Keyboard|rated|Please|action|activationinput|doModal|json|replace|xbmc|getText|sys|was|Duplicate|to_string|47|firstpart|translatePath|ares_rate_url|error|there|Sorry|Agent|autopassword|def|with|else|isinresponse|Thanks|result|registration|Inserted|accepted|Already|already|enter|user|time|http|jsonstring|Your|User|open|activation|read|awaiting_activation|rateaddon|Incorrect|select|ratebuild|excluding|xbmcaddon|now|incorrectpassword|register|datapath|colortag|this|ares_rate_result|your|userinfo|closetag|raterepo|dialog|150|stars|107|close|139|opentag|stripcolortags|activationcode|setHiddenInput|addonid|addon|An|device|many|as|getAddonInfo|search|dump|text|except|find|Activation|showadult|check|registered|getsysinfo|Registered|group|emailsent|You|How|translate|resources|activated|return|n|from|city|path|load|CAPITALS|nameinput|True|bypassed|settings|code|strings|command|minutes|profile|r|address|S|through|couple|shutil|nojson|script|base64|os|isp|re|urllib|try|unique|folder|wizard|random|forget|build|be|dumps|enjoy|Addon|glob|take|is|ip|join|sent|spam|wish|come|pass|Hope|like|repo|must|to|don|php|may|w|you|setSetting|too|ALL|registerresult|username|for|xbmcgui|It|i|in|an|my|s|of|COLOR|deviceid|t".split("|")))
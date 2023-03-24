import requests
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

with open ('links.txt') as l:
    g = l.readlines()

for d in g:
    stripped = (d.rstrip())
    url = stripped+"/about"
    print("Retreiving" + url)
    response = requests.get(url)
    data = response.text
    link = re.findall('''(www.instagram.com.+?)\"''', data)
    try:
        if link == []:
            ytName = re.findall(r"name\">(.+)<\/yt\-formatted-string>", data)
            # with open ('l.txt', 'a') as v:
            #     v.write("No Link"+'\n')
            # print("No Link")        
        else:
            x = (link[0])
            y = x.replace("%2F", '/', 2)
            print(y)    
            with open ('l.txt', 'a') as v:
                v.write('https://'+y+'\n')
            
    except Exception:
        with open ('l.txt', 'a') as v:
            v.write(stripped+"\n")
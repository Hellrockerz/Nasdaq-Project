import re
import instaloader

bot = instaloader.Instaloader()

with open ('l.txt') as l:
    g = l.readlines()

for x in g:
    x = str(x)
    try:
        if not x.startswith("http"):
            print("No Username")
        elif x.startswith("http"):
            y = re.findall(r"com\/(.+)\/", x)
            d = y[0]
            profile = instaloader.Profile.from_username(bot.context, d)
            print("Username: ", profile.followers)
            with open ('username.txt', 'a') as v:
                v.write(d+'\n')
    except:
        Exception
        with open ('username.txt', 'a') as v:
            v.write("No Username"+"\n")

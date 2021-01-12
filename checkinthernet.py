import os
import urllib
from urllib.request import urlopen

active = "Internet is active"
notactive = "No internet connection"

def internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False
if internet():
    print(active)
    w = open('voiceS.txt', 'w')
    t = w.write(active)
    w.close()
    os.system("python3 voiceR.py")
else:
    print("No Internet connection")

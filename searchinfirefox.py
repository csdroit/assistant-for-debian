import os
toS = input(" Enter somthing to searche in firefox : ")
w = open('voiceS.txt', 'w')
voiceS = "thats what i found for " + toS
t = w.write(voiceS)
w.close()
os.system("firefox --search " + toS)
os.system("python3 voiceR.py")
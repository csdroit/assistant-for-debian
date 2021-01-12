 # made by badr

import os

os.system("clear")
os.system("rm voiceR.mp3")

#choices avilable now
print("Active commands ")
print("1- Check inthernet ")
print("2- Search ")
print("98- Informations about project ")
print("99- Quit ")

assistant = int(input("Your choice : "))

if assistant==1:
    os.system("python3 checkinthernet.py")
elif assistant==2:
    os.system("python3 searchinfirefox.py")
elif assistant==98:
    print(" \twixios\n\tMADE BY BADR \n\tv1.0 ")
elif assistant==99:
    quit
else:
    print("not valid")
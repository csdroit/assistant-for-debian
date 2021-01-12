from gtts import gTTS
import os

lan = 'en'
w = open('voiceS.txt', 'r')
t = w.read()
assistantV = gTTS(text=t ,lang=lan ,slow=False)
assistantV.save("voiceR.mp3")
os.system("chmod +x voicsR.mp3")
os.system("mpg123 voiceR.mp3 ")
os.system("python3 assistant.py")


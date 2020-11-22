from gtts import gTTS
import os
a=1
while(True):
    text=raw_input('want you want me to speak:')
    tts = gTTS(text, lang='en')
    tts.save("pcvoice.mp3")
    os.system("start pcvoice.mp3")
    if(a==0):
        exit(0)

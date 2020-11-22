from gtts import gTTS
import speech_recognition as sr
import os
import RPi.GPIO as gp
gp.setmode(gp.BOARD)
gp.setwarnings(False)
gp.setup(11,gp.OUT) #fan tmroom
gp.setup(12,gp.OUT)#fan tmroom
gp.output(12,gp.LOW)
gp.setup(13,gp.OUT) #light tmroom
gp.setup(15,gp.OUT) #light tmroom
gp.output(15,gp.LOW)
gp.setup(16,gp.OUT) #all_fan mainroom set1
gp.setup(18,gp.OUT) #all_fan mainroom set1
gp.output(18,gp.LOW)
gp.setup(22,gp.OUT) #all_fan mainroom set2
gp.setup(32,gp.OUT) #all_fan mainroom set2
gp.output(32,gp.LOW)
gp.setup(29,gp.OUT) #all_fan mainroom set3
gp.setup(31,gp.OUT) #all_fan mainroom set3
gp.output(31,gp.LOW)
gp.setup(33,gp.OUT) #all_lights mainroom set1
gp.setup(35,gp.OUT) #all_ligths mainroom set1
gp.output(35,gp.LOW)
gp.setup(36,gp.OUT) #all_fan sop set1
gp.setup(38,gp.OUT) #all_fan sop set1
gp.output(38,gp.LOW)
gp.setup(37,gp.OUT) #all_lights sop set1
gp.setup(40,gp.OUT) #all_lights sop set1
gp.output(40,gp.LOW)
r = sr.Recognizer()
while(True):
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("done, listening")
    try:
        print(r.recognize_google(audio))
        a=r.recognize_google(audio)
        if(a=="turn on the fan in manager room"):
            text="fan turned on!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(11,gp.HIGH)
       elif(a=="turn of the fan in manager room"):
            text="fan turned off!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(11,gp.LOW)
        elif(a=="turn on the light in manager room"):
            text="light turned on!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(13,gp.HIGH)
        elif(a=="turn of the light in manager room"):
            text="light turned off!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(13,gp.LOW)
        elif(a=="turn on the fan set 1 in main room"):
            text="fans 1 turned on!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(16,gp.HIGH)
        elif(a=="turn of the fan set 1 in main room"):
            text="fans set 1 turned off!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(16,gp.LOW)
        elif(a=="turn on the fans set 2 in main room"):
            text="fans set 2 turned on!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(22,gp.HIGH)
        elif(a=="turn of the fan set 2 in main room"):
            text="fans set 2 turned off!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(22,gp.LOW)
        elif(a=="turn on the fans set 3 in main room"):
            text="fans set 3 turned on!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(29,gp.HIGH)
        elif(a=="turn of the fan set 3 in main room"):
            text="fans set 3 turned off!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(29,gp.LOW)
        elif(a=="turn on the lights in main room"):
            text="lights turned on!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(33,gp.HIGH)
        elif(a=="turn of the lights in main room"):
            text="lights turned off!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(33,gp.LOW)
        elif(a=="turn on the fans in long room"):
            text="fans turned on!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(36,gp.HIGH)
        elif(a=="turn of the fans in long room"):
            text="lights turned off!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(36,gp.LOW)
        elif(a=="turn on the lights in long room"):
            text="lights turned on!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(37,gp.HIGH)
        elif(a=="turn of the lights in long room"):
            text="lights turned off!!";
            tts = gTTS(text, lang='en')
            tts.save("pcvoice.mp3")
            os.system("start pcvoice.mp3")
            gp.output(37,gp.LOW)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

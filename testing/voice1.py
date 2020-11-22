import speech_recognition as sr
 
# Record Audio
r = sr.Recognizer()
while(True):
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio))
        a=r.recognize_google(audio)
        if(a=="turn on the fan"):
            print("fan turned on!!")
        if(a=="turn on the lights"):
            print("lights turned on!!")
        if(a=="turn off the fan"):
            print("fan turned off!!")
        if(a=="turn off the lights"):
            print("lights turned off!!")
        if(a=="exit"):
            print("bye")
            exit(0)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

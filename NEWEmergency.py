
from audo_files import *
import speech_recognition as sr



r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        respond_to_request(text)


    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))

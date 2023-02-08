
from audo_files import *
from audo_files import greeting
import speech_recognition as sr


emergency_status = "off"

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        if "linda" in text.lower():
            if "emergency mode on" or "emergency" in text:
                if emergency_status == "off":
                    emergency_status = "on"
                    emergency_mode_on()
            elif "911" in text:
                if emergency_status == "on":
                    pygame.mixer.music.load("audio/synthesized_audio (4).mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    print("calling 911")
            elif "hospital" or "take me to the hospital" or "to the hospital" in text.lower():
                if emergency_status == "on":
                    pygame.mixer.music.load("audio/synthesized_audio (3).mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    print("going to the nearest hospital")
            elif "emergency mode off" or "emergency off" in text.lower():
                if emergency_status == "on":
                    emergency_status = "off"
                    emergency_mode_off()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))

from utilty import *
from text_to_speech import TextToSpeech


################################################################################################################################################
################################################################################################################################################

def start_conversation():
    tts = TextToSpeech()
    tts.load_translations("translations.csv")

    tts.speak("Hello, this is your assistant Linda, how can I help you today?")

    while True:
        try:
            voice_input = input("Please speak your request: ")
            # tts.speak("Please wait while I process your request...")
            # print("Please wait while I process your request...")
            request = process_input(voice_input)

            if "linda" in request:
                get_linda_response(tts)

            elif "weather" in request:
                get_weather(tts)

            elif "date" in request:
                get_date(tts)

            elif "time" in request:
                get_time(tts)

            elif "thank" in request and "you" in request:
                tts.speak("You're welcome! Have a nice day!")
                print("You're welcome! Have a nice day!")

            elif "safety" in request:
                get_safety(tts)

            elif "self" in request and "driving" in request:
                get_self_driving(tts)

            elif "seat" in request and "belt" in request:
                seat_belt_safety(tts)

            elif "tire" in request and "pressure" in request:
                tire_pressure_safety(tts)

            elif "give" in request and "me" in request and "car" in request and "safety" and "information" in request:
                get_safety_info(tts)

            elif "unlock" in request:
                unlock_car(tts)

            elif "lock" in request:
                lock_car(tts)

            elif "start" in request:
                start_car(tts)

            elif "stop" in request:
                stop_car(tts)

            elif "lights" in request:
                turn_on_lights(tts)

            elif "air" in request and "conditioning" in request:
                turn_on_air_conditioning(tts)

            elif "music" in request:
                play_music(tts)

            elif "open left door" in request:
                open_car_door(tts, "left")

            elif "open right door" in request:
                open_car_door(tts, "right")

            elif "emergency" in request:
                emergency_prompt(tts)
            elif "what" in request and "is" in request and "the" in request and "definition" in request and "of" in request:
                word = request.split( )
                find_definition(tts, word[-1])


            else:
                tts.speak(
                    "I'm sorry, I didn't understand your request. Please try again.")
                print("I'm sorry, I didn't understand your request. Please try again.")

        except Exception as e:
            tts.speak("I'm sorry, an error occurred. Please try again.")
            print("I'm sorry, an error occurred. Please try again.")

################################################################################################################################################
################################################################################################################################################


if __name__ == '__main__':  
    start_conversation()
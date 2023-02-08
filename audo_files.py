from voice import speech
import datetime
import pygame


def emergency_mode_on():
    pygame.init()
    pygame.mixer.music.load("audio/synthesized_audio (17).mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Emergency mode on")
    pygame.mixer.music.load("audio/synthesized_audio (2).mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def emergency_mode_off():
    pygame.init()
    pygame.mixer.music.load("audio\synthesized_audio (18).mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Emergency mode off")


def greeting():

    def greeting_1():
        speech("Hello! How can I assist you today?")
        pygame.init()
        pygame.mixer.music.load("speech.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        print("Hello! How can I assist you today?")

    def greeting_2():
        print("Hi there! How may I help you?")

    def greeting_3():
        print("Good day! What can I do for you?")

    def greeting_4():
        print("Greetings! What can I assist you with?")


def check_information():
    speech("Let me check that for you. One moment please.")
    pygame.init()
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("Let me check that for you. One moment please.")


def perform_task():
    print("Of course, I'd be happy to do that for you.")


def difficult_request():
    print("I'm sorry, I may not be able to do that. However, I'll do my best to find a solution for you.")


def unclear_request():
    print("I'm sorry, could you please rephrase or clarify your request?")


def task_completion():
    print("The task has been completed successfully.")


def end_conversation():
    print("If there's anything else I can help with, don't hesitate to ask. Have a great day!")


def respond_to_request(request):
    if request == "What's the weather today?":
        return "I can check that for you. Where are you located?"

    elif request == "What's the current time?":
        return "The current time is " + str(datetime.now().time()) + ". Can I help with anything else?"

    elif request == "Can you book a flight to New York?":
        return "Sure, what dates are you looking to travel and how many passengers will be traveling?"

    elif request == "What's the latest news?":
        return "I can look that up for you. Which topics are you interested in?"

    elif request == "What are some good restaurants in the area?":
        return "I can search for top-rated restaurants in your area. Can you give me your location and type of cuisine you're interested in?"

    elif request == "What are some popular tourist destinations in France?":
        return "Some popular tourist destinations in France include Paris, Nice, Marseille, and Bordeaux. Is there a specific city you would like more information on?"

    elif request.startswith("What are the ingredients for a chocolate cake?"):
        return "Here's a simple recipe for a chocolate cake: flour, sugar, cocoa powder, baking powder, baking soda, salt, eggs, buttermilk, oil, and vanilla extract. Would you like me to find a specific recipe for you?"

    elif request.startswith("Who won the Oscars this year?"):
        return "I can look that up for you. Which year's Oscars are you interested in?"

    elif request == "What's the exchange rate between USD and EUR?":
        return "The current exchange rate between USD and EUR is [insert exchange rate]. This may fluctuate, would you like me to check again later?"

    elif request.startswith("What's the definition of"):
        word = request.split(" ")[-1]
        return "The definition of " + word + " is [insert definition]. Would you like me to find more information or synonyms for the word?"

    else:
        return "I'm sorry, I don't understand your request. Could you please rephrase it or provide more information?"

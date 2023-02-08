from voice import speech
import datetime
import pygame



def speech_path(request):
    pygame.init()
    pygame.mixer.music.load(request)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


emergency_status = "off"


def respond_to_request(request):
    global emergency_status 
    if request == "What's the weather today".lower():
        speech_path("audio/synthesized_audio (70).mp3")
        return "I can check that for you. Where are you located?"
    elif request == "What's the current time?".lower():
        speech_path("audio/synthesized_audio (70).mp3")
        return "The current time is " + str(datetime.now().time()) + ". Can I help with anything else?"
    elif request == "Can you book a flight to New York?".lower():
        speech_path("audio/synthesized_audio (70).mp3")
        return "Sure, what dates are you looking to travel and how many passengers will be traveling?"
    elif request == "What's the latest news?".lower():
        speech_path("audio/synthesized_audio (70).mp3")
        return "I can look that up for you. Which topics are you interested in?"
    elif request == "What are some good restaurants in the area?".lower():
        speech_path("audio/synthesized_audio (70).mp3")
        return "I can search for top-rated restaurants in your area. Can you give me your location and type of cuisine you're interested in?"
    elif request == "What are some popular tourist destinations in France?".lower():
        speech_path("audio/synthesized_audio (70).mp3")
        return "Some popular tourist destinations in France include Paris, Nice, Marseille, and Bordeaux. Is there a specific city you would like more information on?"
    elif request.startswith("What are the ingredients for a chocolate cake?".lower()):
        speech_path("audio/synthesized_audio (70).mp3")
        return "Here's a simple recipe for a chocolate cake: flour, sugar, cocoa powder, baking powder, baking soda, salt, eggs, buttermilk, oil, and vanilla extract. Would you like me to find a specific recipe for you?"
    elif request.startswith("Who won the Oscars this year?".lower()):
        speech_path("audio/synthesized_audio (70).mp3")
        return "I can look that up for you. Which year's Oscars are you interested in?"
    elif request == "What's the exchange rate between USD and EUR?".lower():
        speech_path("audio/synthesized_audio (70).mp3")
        return "The current exchange rate between USD and EUR is [insert exchange rate]. This may fluctuate, would you like me to check again later?"
    elif request.startswith("What's the definition of".lower()):
        word = request.split
    elif "emergency mode on" in request or "emergency" in request:
        if emergency_status == "off":
            emergency_status = "on"
            speech_path("audio/synthesized_audio (17).mp3")
            speech_path("audio/synthesized_audio (2).mp3")
    elif "911" in request:
        if emergency_status == "on":
            speech_path("audio/synthesized_audio (4).mp3")
            print("calling 911")
    elif "hospital" or "take me to the hospital" or "to the hospital" in request.lower():
        if emergency_status == "on":
            speech_path("audio/synthesized_audio (3).mp3")
            print("going to the nearest hospital")
    elif "emergency mode off" or "emergency off" in request.lower():
        if emergency_status == "on":
            emergency_status = "off"
            speech_path("audio/synthesized_audio (18).mp3")
    elif "emergency mode off" or "emergency off" in request.lower():
        if emergency_status == "on":
            emergency_status = "off"
            speech_path("audio/synthesized_audio (18).mp3")

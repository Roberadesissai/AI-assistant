
import requests
import datetime
import pygame
import random
from face_reco_video import face


def speech_path(request):
    pygame.init()
    pygame.mixer.music.load(request)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

auto_drive_status="off"
safe_mode_status="on"


def greet_time_of_day():
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 12:
        speech_path("audio/synthesized_audio (37).mp3")

    elif hour >= 12 and hour < 17:
        speech_path("audio/synthesized_audio (38).mp3")

    elif hour >= 17:
        speech_path("audio/synthesized_audio (39).mp3")


def check_door(door_status, door_position):
    if door_status == "unlocked":
        if door_position == "right":
            speech_path("audio#2/synthesized_audio (1).mp3")

        elif door_position == "left":
            speech_path("audio#2/synthesized_audio (2).mp3")
    else:
        speech_path("audio/synthesized_audio.mp3")


def door_status(door):
    if door == "right":
        speech_path("audio/synthesized_audio (24).mp3")

    elif door == "left":
        speech_path("audio/synthesized_audio (25).mp3")

    else:
        print("Invalid door input")


def check_weather():
    api_key = "cedda2dc71c6e1ead83c6254e376d728"
    city_id = 4522411
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&id=" + str(city_id)
    response = requests.get(complete_url)
    weather_data = response.json()

    weather_main = weather_data["weather"][0]["main"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]

    print("The weather is: ", weather_description)
    print("Temperature: ", temperature)
    print("Humidity: ", humidity)
    print("Pressure: ", pressure)

    if weather_main in ["Rain", "Thunderstorm", "Snow"]:
        speech_path("audio/synthesized_audio (26).mp3")
        print("The weather is bad. Don't drive today.")
    else:
        print("The weather is good. You can drive today.")

def start_ride():
    speech_path("audio/synthesized_audio (40).mp3")
    speech_path("audio/synthesized_audio (41).mp3")
    speech_path("audio/synthesized_audio (42).mp3")
    speech_path("audio/synthesized_audio (43).mp3")
    speech_path("audio/synthesized_audio (44).mp3")
    speech_path("audio/synthesized_audio (45).mp3")
    speech_path("audio/synthesized_audio (46).mp3")
    print("Safe mode activated!")

def check_safe_mode(safe_mode_status):
    if safe_mode_status == "off":
        speech_path("audio#2/synthesized_audio (3).mp3")
        safe_mode_status = "on"
    elif safe_mode_status == "on":
        return ("Safery mode activated!")


def check_auto_drive(request):

    global auto_drive_status
    if request == "auto drive on" or request == "turn auto drive on".lower():
        if auto_drive_status == "off":
            speech_path("audio/synthesized_audio (10).mp3")
            auto_drive_status = "on"
        else:
            speech_path("audio/synthesized_audio (12).mp3")
            auto_drive_status = "off"
    elif request == "auto drive off" or request == "turn auto drive off".lower():
        if auto_drive_status == "on":
            speech_path("audio/synthesized_audio (13).mp3")
            auto_drive_status = "off"
        else:
            speech_path("audio/synthesized_audio (10).mp3")
            auto_drive_status = "on"
    
    pass

def damage_detector():
    speech_path("audio/synthesized_audio (47).mp3")

def task_completed():
    speech_path("audio/synthesized_audio (64).mp3")
    speech_path("audio/synthesized_audio (65).mp3")

unknown_detect=["audio/synthesized_audio (66).mp3","audio/synthesized_audio (67).mp3","audio/synthesized_audio (68).mp3","audio/synthesized_audio (69).mp3"]
def detect_faces():
    if  "Robera" in face:
        speech_path("audio#2/synthesized_audio (4).mp3")
    elif  "Mati" in face:
        speech_path("audio#2/synthesized_audio (5).mp3")

def unknown_face():
    if  "Unknown" in face:
        speech_path(random.choice(unknown_detect))

def run_random_function():
    functions = [greet_time_of_day, unknown_face]
    selected_function = random.choice(functions)
    selected_function()


linda_respond = ["audio/synthesized_audio (11).mp3", "audio/synthesized_audio (27).mp3", "audio/synthesized_audio (28).mp3", "audio/synthesized_audio (29).mp3", "audio/synthesized_audio (30).mp3",
    "audio/synthesized_audio (31).mp3", "audio/synthesized_audio (32).mp3", "audio/synthesized_audio (33).mp3", "audio/synthesized_audio (34).mp3", "audio/synthesized_audio (35).mp3", "audio/synthesized_audio (36).mp3"]


def respond_to_request(request):

    if request == "Linda" or request == "linda".lower() or request == "hey linda".lower() or request == "hey Linda":
        speech_path(random.choice(linda_respond))

    elif request == "What's the weather today".lower():
        speech_path("audio/synthesized_audio (70).mp3")

    elif request == "tell me who you are" or request == "who are you".lower():
        speech_path("audio/synthesized_audio (16).mp3")

    elif request == "let's go":
        speech_path("audio/synthesized_audio (19).mp3")

    elif request == "check weather" or request == "check the weather".lower():
        pass
    elif request == "check safe mode" or request == "check safe mode".lower():
        pass
    elif request == "check auto drive" or request == "check auto drive".lower():
        pass
    elif request == "check door" or request == "check door".lower():
        pass
    elif request == "start ride" or request == "start ride".lower():
        pass
    elif request == "there is a damage in the car" or request == "there is a damge in the car" or request == "damage detector".lower() or request == "damage detect"or request == "there is a damge on the car":
        speech_path("audio/synthesized_audio (48).mp3")
    elif request == "play music" or request == "open music".lower():
        speech_path("audio/synthesized_audio (50).mp3")
    elif request == "change the air conditioning" or request == "change the temperture".lower():
        speech_path("audio/synthesized_audio (51).mp3")
        if request == "Yes" or request == "yes".lower():
            speech_path("audio/synthesized_audio (52).mp3")
    elif request == "find a gas station" or request == "nearest gas station".lower() or request == "find a nearest gas station" or request == "gas station":
        speech_path("audio/synthesized_audio (53).mp3")
    elif request == "what is estimated time of arrival" or request == "what is my estimated time of arrival".lower() or request == "time of arrival" or request == "estimated time":
        speech_path("audio/synthesized_audio (54).mp3")
    elif request == "open the sun roof" or request == "sun roof open".lower():
        speech_path("audio/synthesized_audio (55).mp3")
    elif request == "close the sun roof" or request == "sun roof close".lower():
        speech_path("audio/synthesized_audio (56).mp3")
    elif request == "What are some popular tourist destinations in France".lower():
        speech_path("audio/synthesized_audio (57).mp3")
    elif request == "What are the ingredients for a chocolate cake".lower():
        speech_path("audio/synthesized_audio (58).mp3")
        if request == "Yes" or request == "yes".lower():
            pass
    elif request == "can you book a flight to New York".lower() or request == 'book a flight to New York'.lower():
        speech_path("audio/synthesized_audio (59).mp3")
        if request == "Yes" or request == "yes".lower():
            speech_path("audio/synthesized_audio (60).mp3")
    elif request == "check" or request == "check for me".lower():
        speech_path("audio/synthesized_audio (61).mp3")
    elif request == "can you pass the speed limit" or request == "pass speed limit".lower():
        speech_path("audio/synthesized_audio (62).mp3")
    elif request == "can you pass the fuel limit" or request == "pass fuel limit".lower():
        speech_path("audio/synthesized_audio (63).mp3")
    elif request == "let's go to nearest restaurant" or request == "nearest restaurant".lower() or request == "go to nearest restaurant".lower() or request == "find nearest restaurant".lower():
        speech_path("audio#2/synthesized_audio (6).mp3")
        if request == "yes" or request == "yes".lower():
            speech_path("audio#2/synthesized_audio (7).mp3")
    elif request == "shut down system".lower() or request == "power off".lower():
        exit()

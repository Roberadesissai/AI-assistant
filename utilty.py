import random
import csv
from re import search
from text_to_speech import TextToSpeech
from datetime import datetime
import googlemaps
from datetime import datetime
from weather import get_weather_data
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from twilio.rest import Client



################################################################################################################################################
################################################################################################################################################




################################################################################################################################################
################################################################################################################################################


def process_input(voice_input):
    # Convert voice input to lowercase and remove punctuation
    voice_input = voice_input.lower()
    voice_input = voice_input.strip('.,?!_ ')

    # Split input into words and return as list
    return voice_input.split()


def get_weather(tts):
    tts.speak("Please wait while I retrieve the weather information...")
    print("Please wait while I retrieve the weather information...")
    weather, temp = get_weather_data()
    if weather and temp:
        tts.load_translations("translations.csv")
        translation = f"The weather is {weather} and it's {temp:.2f} degrees Celsius."
        print(translation)
        tts.speak(translation)

        if 'clouds' in weather or 'clear' in weather:
            tts.speak("It's safe to drive. Please be careful on the road.")
        else:
            tts.speak("It's not safe to drive. Please avoid driving if possible.")


def get_date(tts):
    tts.speak("Please wait while I retrieve the date information...")
    print("Please wait while I retrieve the date information...")

    # Get current date and format as speech text
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    speech_text = f"Today's date is {current_date}."
    tts.speak(speech_text)
    print(speech_text)


def get_time(tts):
    tts.speak("Please wait while I retrieve the time information...")
    print("Please wait while I retrieve the time information...")

    # Get current time and format as speech text
    current_time = datetime.now().strftime("%I:%M %p")
    speech_text = f"The current time is {current_time}."
    tts.speak(speech_text)
    print(speech_text)


def get_safety(tts):
    tts.speak("Car safety is a very important topic. When driving, you should always wear your seatbelt and obey traffic laws. You should also maintain your vehicle and keep it in good condition. In addition, you should avoid distractions such as using your phone or eating while driving. Finally, you should always drive defensively and be prepared for unexpected situations on the road.")


def get_self_driving(tts):
    tts.speak("Self-driving cars are a relatively new technology, but they are becoming more and more common on the roads.")
    tts.speak("These cars use a combination of sensors, cameras, and advanced software to navigate the roads and avoid obstacles.")
    tts.speak("One of the biggest advantages of self-driving cars is that they can potentially reduce the number of accidents on the roads.")
    tts.speak("They can also be more fuel-efficient than traditional cars because they are designed to optimize driving conditions.")
    tts.speak("However, there are still some concerns about the safety of self-driving cars, and regulations are still being developed to ensure that they meet strict safety standards.")
    tts.speak("Overall, self-driving cars have the potential to revolutionize the way we travel, but we still have a long way to go before they become a common sight on the roads.")


def seat_belt_safety(tts):
    tts.speak("Wearing a seat belt is one of the most important things you can do to stay safe while driving. Seat belts can help prevent serious injury or death in the event of an accident. It's important to always wear your seat belt, and to make sure that all passengers in your car are wearing their seat belts as well.")
    print("Wearing a seat belt is one of the most important things you can do to stay safe while driving. Seat belts can help prevent serious injury or death in the event of an accident. It's important to always wear your seat belt, and to make sure that all passengers in your car are wearing their seat belts as well.")


def tire_pressure_safety(tts):
    tts.speak(
        "Maintaining proper tire pressure is an important part of car safety. Overinflated or underinflated")


def get_safety_info(tts):
    airbag_info = "The car is equipped with multiple airbags to ensure your safety in case of a collision."
    lane_assist_info = "The car is equipped with lane assist technology that keeps the car within the lane markings."
    emergency_brake_info = "The car is equipped with an emergency brake system that automatically applies the brakes if it detects an imminent collision."

    # Generate speech for car safety information
    speech_text = f"{airbag_info} {lane_assist_info} {emergency_brake_info}"
    tts.speak(speech_text)
    print(speech_text)


def get_linda_response(tts):
    responses = ["How can I assist you?", "What can I do for you today?",
                 "What's on your mind?", "How can I make your ride more comfortable?", "What do you need?"]
    random_response = random.choice(responses)
    tts.speak(random_response)
    print(random_response)


def unlock_car(tts):
    tts.speak("Please wait while I unlock the car...")
    print("Please wait while I unlock the car...")
    # Code to send signal to unlock the car


def lock_car(tts):
    tts.speak("Please wait while I lock the car...")
    print("Please wait while I lock the car...")
    # Code to send signal to lock the car


def start_car(tts):
    tts.speak("Please wait while I start the car...")
    print("Please wait while I start the car...")
    # Code to start the car


def stop_car(tts):
    tts.speak("Please wait while I stop the car...")
    print("Please wait while I stop the car...")
    # Code to stop the car


def turn_on_lights(tts):
    tts.speak("Please wait while I turn on the lights...")
    print("Please wait while I turn on the lights...")
    # Code to turn on the lights


def turn_on_air_conditioning(tts):
    tts.speak("Please wait while I turn on the air conditioning...")
    print("Please wait while I turn on the air conditioning...")
    # Code to turn on the air conditioning


def play_music(tts):
    # Set up Spotify API authentication
    scope = "user-read-playback-state,user-modify-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # Get user's Spotify username
    username = sp.me()['id']

    # Get user's request for what to play
    tts.speak("What would you like me to play?")
    request = input("What would you like me to play? ")

    # Search Spotify for the request
    results = sp.search(q=request, type='track')

    # Check if any results were found
    if len(results['tracks']['items']) == 0:
        tts.speak("I'm sorry, I could not find that song.")
        print("I'm sorry, I could not find that song.")
        return

    # Get the first track in the search results
    track_uri = results['tracks']['items'][0]['uri']

    # Play the track on the user's Spotify account
    sp.start_playback(device_id=None, context_uri=None,
                      uris=[track_uri], offset=None)
    tts.speak("Playing " + results['tracks']['items'][0]['name'] +
              " by " + results['tracks']['items'][0]['artists'][0]['name'])
    print("Playing " + results['tracks']['items'][0]['name'] +
          " by " + results['tracks']['items'][0]['artists'][0]['name'])


def unlock_car(tts):
    tts.speak("Please wait while I unlock the car...")
    print("Please wait while I unlock the car...")
    # Code to send signal to unlock the car


def lock_car(tts):
    tts.speak("Please wait while I lock the car...")
    print("Please wait while I lock the car...")
    # Code to send signal to lock the car


def start_car(tts):
    tts.speak("Please wait while I start the car...")
    print("Please wait while I start the car...")
    # Code to start the car


def stop_car(tts):
    tts.speak("Please wait while I stop the car...")
    print("Please wait while I stop the car...")
    # Code to stop the car


def turn_on_air_conditioning(tts):
    tts.speak("Please wait while I turn on the air conditioning...")
    print("Please wait while I turn on the air conditioning...")
    # Code to turn on the air conditioning


def open_car_door(tts, side):
    tts.speak(f"Please wait while I open the {side} door...")
    print(f"Please wait while I open the {side} door...")
    # Code to open the specified car door


def random_response(tts):
    responses = ["Okay", "Sure", "No problem", "Got it"]
    responses = random.choice(responses)
    tts.speak(random_response(responses))


def find_nearby_places(api_key, place_type):
    gmaps = googlemaps.Client(key=api_key)

    # Geocoding an address
    geocode_result = gmaps.geocode(
        '1600 Amphitheatre Parkway, Mountain View, CA')

    # Use the latitude and longitude of the address to search for nearby places
    location = geocode_result[0]['geometry']['location']
    nearby_places_result = gmaps.places_nearby(
        location=location, radius=10000, type=place_type)

    # Get the name and address of the first result
    if len(nearby_places_result['results']) > 0:
        name = nearby_places_result['results'][0]['name']
        address = nearby_places_result['results'][0]['vicinity']
        return f"The nearest {place_type} is {name} at {address}"
    else:
        return f"No {place_type} found nearby"


def pre_ride_questions(tts):
    # Ask for the passenger's name
    tts.speak("What is your name?")
    name = input("What is your name? ")

    # Ask for the pickup location
    tts.speak("Where would you like to be picked up?")
    pickup_location = input("Where would you like to be picked up? ")

    # Ask for the destination
    tts.speak("Where would you like to go?")
    destination = input("Where would you like to go? ")

    # Confirm the information with the passenger
    tts.speak(
        f"Thank you, {name}. I understand that you would like to be picked up at {pickup_location} and go to {destination}. Is that correct?")
    response = input(
        f"Thank you, {name}. I understand that you would like to be picked up at {pickup_location} and go to {destination}. Is that correct? ")

    # If the passenger confirms, return the information as a dictionary
    if response.lower() == "yes":
        return {"name": name, "pickup_location": pickup_location, "destination": destination}
    else:
        # If the passenger doesn't confirm, ask for the information again
        return pre_ride_questions(tts)


def confirm_driver(tts, driver_name):
    # Ask the passenger if the driver is correct
    tts.speak("The passenger is " + driver_name + ". Is that correct?")
    response = input("The passenger is " + driver_name + ". Is that correct? ")

    # Check if the response is affirmative
    if response.lower() in ["yes", "yep", "correct", "right", "yeah", "sure"]:
        tts.speak("Great. Let's start the ride.")
        return True
    else:
        tts.speak(
            "I'm sorry, I'll need to confirm the driver's identity before we can start the ride.")
        return False


def get_name():
    name = input("Please enter your name: ")
    return name

# Function to check if user's name is in the CSV file


def check_name(name):
    with open("names.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if name in row:
                return True
    return False

# Function to add user's name to the CSV file


def add_name(name):
    with open("names.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name])

# Function to welcome the user by name


def welcome(name):
    greetings = ["Hello", "Hi", "Welcome"]
    greeting = random.choice(greetings)
    print(f"{greeting}, {name}!")


def main():
    name = get_name()
    if check_name(name):
        welcome(name)
    else:
        add_name(name)
        print("Nice to meet you!")


def find_definition(tts, word):
    # Send a GET request to the Merriam-Webster Dictionary API to retrieve the definition
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}"
    response = requests.get(
        url, params={"key": "8ab319f9-54a3-44b6-bc5b-575c312ba3f8"})

    # Parse the response JSON to extract the definition
    response_json = response.json()
    if isinstance(response_json, list):
        # If the API returns a list of words, use the first word
        response_json = response_json[0]

    if "shortdef" in response_json:
        # If the API returns a definition, extract and say the first definition
        definition = response_json["shortdef"][0]
        tts.speak(f"The definition of {word} is: {definition}")
        print(f"The definition of {word} is: {definition}")
    else:
        # If the API does not return a definition, say that no definition was found
        tts.speak(f"I'm sorry, I could not find a definition for {word}")
        print(f"I'm sorry, I could not find a definition for {word}")


def turn_on_smart_switch():
    url = "https://maker.ifttt.com/trigger/turn_on_smart_switch/with/key/YOUR_IFTTT_KEY"
    response = requests.post(url)

    if response.status_code == 200:
        print("Smart switch turned on successfully.")
    else:
        print("Failed to turn on smart switch.")


def how_to(tts):
    tts.speak("Of course! What do you need help with?")
    request = input("Of course! What do you need help with? ")
    search_query = "how to " + request

    # Use a search engine to find instructions
    try:
        search_results = search(search_query, num_results=1)
        tts.speak("Here are some instructions for " +
                  request + ": " + search_results[0])
    except:
        tts.speak("I'm sorry, I couldn't find instructions for " + request)

def emergency_help(tts):
    tts.speak("In case of an emergency, please call 911 immediately.")

    while True:
        tts.speak("Do you need help turning on emergency mode on your phone?")
        response = input(
            "Do you need help turning on emergency mode on your phone? ").lower()
        if "yes" in response:
            tts.speak("To turn on emergency mode on your phone, go to your phone's settings and look for the emergency options. You should be able to find an option to turn on emergency mode there.")
            break
        elif "no" in response:
            break

    while True:
        tts.speak("Do you need help turning off emergency mode on your phone?")
        response = input(
            "Do you need help turning off emergency mode on your phone? ").lower()
        if "yes" in response:
            tts.speak("To turn off emergency mode on your phone, go to your phone's settings and look for the emergency options. You should be able to find an option to turn off emergency mode there.")
            break
        elif "no" in response:
            break

    while True:
        tts.speak(
            "Do you need information on how to contact medical or emergency services in your area?")
        response = input(
            "Do you need information on how to contact medical or emergency services in your area? ").lower()
        if "yes" in response:
            tts.speak("To contact emergency services in the United States, simply dial 911 from any phone. For non-emergency medical assistance, you can contact your primary care physician or look up local urgent care centers or walk-in clinics.")
            break
        elif "no" in response:
            break

    tts.speak("If you need further assistance, please do not hesitate to ask.")


def help(tts):
    # Introduction and main menu
    tts.speak("How can I help you? Here are some topics I can assist you with:")
    print("How can I help you? Here are some topics I can assist you with:")
    tts.speak("1. Navigation")
    print("1. Navigation")
    tts.speak("2. Music")
    print("2. Music")
    tts.speak("3. Climate control")
    print("3. Climate control")
    tts.speak("4. Safety features")
    print("4. Safety features")
    tts.speak("5. Maintenance")
    print("5. Maintenance")

    # Get user's selection
    tts.speak(
        "Please say the number of the topic you would like more information about.")
    print("Please say the number of the topic you would like more information about.")
    choice = input("Please enter a number: ")

    # Provide information based on user's selection
    if choice == "1":
        # Navigation tips
        tts.speak("Here are some tips for using the car's navigation system:")
        print("Here are some tips for using the car's navigation system:")
        tts.speak(
            "- Use voice commands to search for destinations and get directions.")
        print("- Use voice commands to search for destinations and get directions.")
        tts.speak(
            "- You can also use the touchscreen or physical controls to input destinations and view maps.")
        print("- You can also use the touchscreen or physical controls to input destinations and view maps.")
        tts.speak(
            "- Make sure to update the system's maps regularly for accurate directions.")
        print("- Make sure to update the system's maps regularly for accurate directions.")

    elif choice == "2":
        # Music tips
        tts.speak("Here are some tips for using the car's music system:")
        print("Here are some tips for using the car's music system:")
        tts.speak(
            "- Use voice commands to play specific songs, artists, or playlists.")
        print("- Use voice commands to play specific songs, artists, or playlists.")
        tts.speak(
            "- You can also use the touchscreen or physical controls to browse and play music.")
        print("- You can also use the touchscreen or physical controls to browse and play music.")
        tts.speak(
            "- Connect your smartphone to the car's audio system for more music options.")
        print("- Connect your smartphone to the car's audio system for more music options.")

    elif choice == "3":
        # Climate control tips
        tts.speak("Here are some tips for using the car's climate control system:")
        print("Here are some tips for using the car's climate control system:")
        tts.speak(
            "- Use voice commands or the touchscreen to adjust the temperature, fan speed, and other settings.")
        print("- Use voice commands or the touchscreen to adjust the temperature, fan speed, and other settings.")
        tts.speak("- Enable the auto climate control feature to automatically adjust the temperature based on the outside weather and your preferred settings.")
        print("- Enable the auto climate control feature to automatically adjust the temperature based on the outside weather and your preferred settings.")
        tts.speak(
            "- Use the defrost function to quickly clear fog and ice from the windshield.")
        print(
            "- Use the defrost function to quickly clear fog and ice from the windshield.")

    elif choice == "4":
        # Safety features tips
        tts.speak("Here are some tips for using the car's safety features:")
        print("Here are some tips for using the car's safety features:")
        tts.speak(
            "- Make sure to fasten your seatbelt and ensure all passengers are safe.")


def medical_emergency(tts):
    """
    Initiates a call to emergency services for a medical emergency.
    """
    tts.speak(
        "If you or someone else needs medical attention, please call 911 immediately.")
    tts.speak(
        "If you are not able to make the call yourself, say 'emergency call' and I will dial 911 for you.")
    tts.speak(
        "Please provide as much information about the situation as possible to the emergency operator.")



def emergency_prompt(tts):
    # Prompt the user for the type of emergency
    tts.speak(
        "What type of emergency are you experiencing? Say medical, fire, or police.")
    response = input(
        "What type of emergency are you experiencing? Say medical, fire, or police. ")

    if response.lower() == "medical":
        # Prompt the user for the nature of the medical emergency
        tts.speak("What is the nature of the medical emergency?")
        response = input("What is the nature of the medical emergency? ")

        # Call emergency services with the appropriate information
        tts.speak("Calling emergency services. Please stay on the line.")
        # Call emergency services API with details of the medical emergency

    elif response.lower() == "fire":
        # Prompt the user for the location of the fire
        tts.speak("What is the location of the fire?")
        response = input("What is the location of the fire? ")

        # Call emergency services with the appropriate information
        tts.speak("Calling emergency services. Please stay on the line.")
        # Call emergency services API with details of the fire

    elif response.lower() == "police":
        # Prompt the user for the reason for calling the police
        tts.speak("What is the reason for calling the police?")
        response = input("What is the reason for calling the police? ")

        # Call emergency services with the appropriate information
        tts.speak("Calling emergency services. Please stay on the line.")
        # Call emergency services API with details of the police emergency

    else:
        # If the user does not provide a valid response, inform them and end the conversation
        tts.speak(
            "I'm sorry, I didn't understand your response. Please try again later.")


def medical_emergency(tts, phone_numbers):
    """
    Initiates a call to emergency services for a medical emergency.
    """
    message = "If you or someone else needs medical attention, please call 911 immediately. "\
              "If you are not able to make the call yourself, say 'emergency call' and I will dial 911 for you. "\
              "Please provide as much information about the situation as possible to the emergency operator."
    tts.speak(message)

    # Send the message to all phone numbers in the list
    for number in phone_numbers:
        (tts, number, message)





################################################################################################################################################
################################################################################################################################################



import requests
import json
from text_to_speech import TextToSpeech

def get_weather_data():
    city = "Columbus"  # Replace with the name of the city you want to check the weather for
    api_key = "cedda2dc71c6e1ead83c6254e376d728"  # Replace with your own OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = json.loads(response.text)

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return (weather, temp)
    else:
        print("Error: could not fetch weather data")
        return (None, None)

if __name__ == "__main__":
    weather, temp = get_weather_data()
    if weather and temp:
        tts = TextToSpeech()
        tts.load_translations("translations.csv")
        translation = f"The weather is {weather} and it's {temp:.2f} degrees Celsius."
        print(translation)
        tts.speak(translation)

        if 'clouds' in weather or 'clear' in weather:
            tts.speak("It's safe to drive. Please be careful on the road.")
        else:
            tts.speak("It's not safe to drive. Please avoid driving if possible.")

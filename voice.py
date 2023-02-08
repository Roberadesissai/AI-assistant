import requests

def speech(text, api_key="95348d1a4dd7613119c34a3897ecedce", voice_id="EXAVITQu4vr4xnSDxMaL"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "accept": "audio/mpeg",
        "Content-Type": "application/json"
    }

    data = {
        "text": text
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open("speech.mp3", "wb") as file:
            file.write(response.content)
        print("Speech saved as 'speech.mp3'")
    else:
        print("Request failed with status code:", response.status_code)

speech("Hello, Robera how are you?")
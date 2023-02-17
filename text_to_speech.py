import csv
import os
import requests
import hashlib
import pygame

class TextToSpeech:
    def __init__(self, api_key="02fa6aabbc3008da99e74c3e895afa43", voice_id="EXAVITQu4vr4xnSDxMaL"):
        self.api_key = api_key
        self.voice_id = voice_id
        self.translations = {}

    def load_translations(self, csv_file):
        if os.path.isfile(csv_file):
            with open(csv_file, 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if len(row) != 3:
                        print(f"Error: Row {i+1} of '{csv_file}' does not have the correct number of columns")
                        print(f"Row {i+1}: {row}")
                    else:
                        self.translations[row[0]] = row[1]

    def generate_speech(self, text, filename):
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"

        headers = {
            "xi-api-key": self.api_key,
            "accept": "audio/mpeg",
            "Content-Type": "application/json"
        }

        data = {
            "text": text
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"Speech saved as '{filename}'")
        else:
            print("Error: speech not generated")

    def speak(self, text):
        text_hash = hashlib.sha256(text.encode()).hexdigest()
        if text_hash in self.translations:
            filename = self.translations[text_hash]
        else:
            filename = f"Speech Dataset/speech_{len(self.translations)+1}.mp3"
            self.generate_speech(text, filename)
            self.translations[text_hash] = filename
            with open('translations.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([text_hash, filename, text])
        pygame.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

if __name__ == '__main__':
    ttf = TextToSpeech()
    ttf.load_translations('translations.csv')


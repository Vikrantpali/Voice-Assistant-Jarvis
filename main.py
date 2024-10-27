import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import musicLibrary
import wikipedia
import os
#pip install pocketsphinix
#pip install speech_recognition
#pip install pyttsx3
#pip install wikipedia

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        try:
            link = musicLibrary.get_song_link(song)
            webbrowser.open(link)
        except KeyError:
            speak("Sorry, I couldn't find the song in the library.")
            print(f"Song '{song}' not found in the music library.")
    elif 'wikipedia' in command:
        speak('Searching Wikipedia...')
        query = command.replace("wikipedia", "").strip()
        try:
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("The query is ambiguous. Please be more specific.")
            print("DisambiguationError:", e)
        except wikipedia.exceptions.PageError as e:
            speak("Sorry, I couldn't find a page matching your query.")
            print("PageError:", e)
        except wikipedia.exceptions.WikipediaException as e:
            speak("An error occurred while fetching data from Wikipedia.")
            print("WikipediaException:", e)
    else:
        speak("Sorry, I did not understand the command.")
        print("Command:", command)

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may I help you.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        try:
            with sr.Microphone() as source:
                print("Listening for word 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                wake_word = recognizer.recognize_google(audio, language='en-in').lower()
                
                if "jarvis" in wake_word:
                    wish_me()
                    print("Listening for command...")
                    # Listen for command
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio, language='en-in')
                        process_command(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
        except Exception as e:
            print("An unexpected error occurred: {0}".format(e))

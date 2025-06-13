import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
        except sr.RequestError:
            speak("Network error.")
        return None

# Main loop
speak("Hello! Ask me anything about Wikipedia.")
while True:
    query = listen()
    if query:
        if query.lower() in ['exit', 'quit', 'bye']:
            speak("Goodbye!")
            break
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Topic is too broad, please be more specific.")
        except Exception as e:
            speak("Could not find information. Try another topic.")
    else:
        speak("Please try again.")

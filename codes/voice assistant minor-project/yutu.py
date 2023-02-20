import pyttsx3 # provides engine for text to speech library
import speech_recognition as sr
from datetime import datetime
import os
from requests import get
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id) # voice id of our assistant

def speak(audio): #function to convert text to audio
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good morning sir..")
    elif hour > 12 and hour < 17:
        speak("Good afternoon sir..")
    elif hour > 17:
        speak("Good evening sir..")

    speak("Im Aryan, How can i help you...")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # so that jarvis wont stop when you are not speaking
        audio = r.listen(source, timeout = 5, phrase_time_limit = 5)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        print(query)
    except Exception as e:
        speak("Say that again please..")
        return 'none'
    return query

if __name__ == "__main__":
    wishme()
    # while True:
    if 1:
        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "ip address" in query:
            ip = get("https://api.ipify.org/").text
            speak(f"Your Ip Address is {ip}")

        # elif "command prompt" or "cmd" in query:
        #     npath = "C:\\WINDOWS\\system32\\cmd.exe"
        #     os.startfile(npath)

        elif "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia")
            print(result)
            speak(result)

        # if 'youtube' in query:
        #     speak("Which video or song should i play")
        #     s = takecommand().lower()
        #     kit.playonyt(f"{s}")

        if 'Facebook' in query:
            webbrowser.open('https://www.Facebook.com/')
            speak('opening Facebook sir')

        if 'stack overflow' in query:
            webbrowser.open('https://www.stackoverflow.com/')
            speak('opening stack overflow')
        if 'google' in query:
            speak("sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
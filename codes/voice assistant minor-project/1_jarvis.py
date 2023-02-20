from asyncio import exceptions
from datetime import datetime
from os import name
from unittest import result
from pip import main
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty(voices, voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good morning sir")
    elif hour > 12 and hour < 17:
        speak("Good afternoon sir")
    elif hour > 17:
        speak("Good evening sir")
    
    print("How can i help you...")
    speak("Im Alexandar, Your very personal assistant, How can i help you...")

def takecommand(): #It takes microphone input 
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        r.energy_threshold = 300
        '''We can increase energy threshold to increase the mic power'''
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recoginzing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except exceptions as e: 
        # print(e)

        print("say that again please...")
        return None
    
    return query
if __name__ == "__main__":
    wishme()
    while (10>5):
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2 )
            speak("According to wikipedia")
            print(results)
            speak(results)

        if 'cuims' in query:
            webbrowser.open('https://uims.cuchd.in/uims/')

        if 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')
            speak('opening Youtube sir')

        if 'blackboard' in query:
            webbrowser.open('https://cuchd.blackboard.com/ultra/course')

        if 'music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=B4Exdiw1bWg&list=RDEMcSTwEn6xdRFUAE7GbTtqgQ&index=2")

        if 'stop' or 'exit' in query:
            break
        
        elif 'open Gmail' or 'open my mail' or 'open my Gmail' in query:
            speak("i dont knot")

        if ' joke ' or 'funny' in query:
            speak(pyjokes.get_joke())


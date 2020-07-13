import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.getProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning, Sir!")
    elif hour > 12 and hour < 18:
        speak("Good Evening, Sir!")
    elif hour > 18 and hour < 24:
        speak("Good Night Sir! Sleep Well")
    else:
        speak("Welcome Back, Sir!")

    speak("How may I help You Sir")


def takeCommand():
    r = sr.Recognizer()

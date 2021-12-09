import datetime
import webbrowser as wb
import wikipedia
import speech_recognition as sr
import pyaudio
import os
import smtplib
import pyttsx3
import time
import selenium

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Jarvis Voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Jarvis Listening
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please!!!")
        return "None"
    return query

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good ofternoon!")
    else:
        speak("Good Evening!")
    speak("Hello fucker, I am Your Monkey Voice assistant ,How may i help you.")

wb.register('chrome',None,wb.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application \\chrome.exe"))
 
# Main function
mainBool = True

if __name__=="__main__":
    while mainBool:
        query = takecommand().lower()
        # Logic for tasks depending on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query,sentences=2)
            speak("From the wikipedia")
            speak(results)
        elif 'open youtube' in query:
            url = 'http://youtube.com/'
            wb.get('chrome').open_new(url)
            time.sleep(10)
        elif 'get from youtube' in query:
            speak('What i need to find')
            query = takecommand().lower()
            if query != "":
                search_string = query.replace(" ", "+")
                url = 'http://youtube.com/results?sp=mAEA&search_query=' + search_string
                wb.get('chrome').open_new(url)
                time.sleep(10)
        elif 'get into mood' in query:
            url = 'http://youtube.com/watch?v=OPf0YbXqDm0'
            wb.get('chrome').open_new(url)
            time.sleep(10)
        elif 'open google' in query:
            url = 'http://google.com'
            wb.get('chrome').open_new(url)
        elif 'hello' in query:
            wishme()
        elif 'check my mail' in query:
            url = 'http://gmail.com'
            wb.get('chrome').open_new(url)
        elif 'internshala' in query:
            url = 'http://internshala.com'
            wb.get('chrome').open_new(url) 
        elif 'google' in query:
            speak('What i need to google')
            query = takecommand().lower()
            search_string = query.replace(' ','+')
            for i in range(1):
                wb.get('chrome').open_new("https://www.google.com/search?q=" + search_string +"&start=" + str(i))
        elif 'open code' in query:
            codepath = "C:\\Users\\Bejjanki KalyanReddy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'close code' in query:
            codepath = "C:\\Users\\Bejjanki KalyanReddy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.close(1)
        elif 'anything on whatsapp' in query:
            codepath = "C:\\Users\\Bejjanki KalyanReddy\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codepath)
        elif 'who are you' in query:
            speak("I am Friday , Female voice assistant created by kalyan reddy , i was written in python , i can do severeal tasks in PC.")
        elif 'game development' in query:
            codepath = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
            os.startfile(codepath)
        elif 'bye bye' in query:
            mainBool = False
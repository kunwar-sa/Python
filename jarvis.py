import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechRecognitiom
import wikipedia # pip install wikipedia
import webbrowser
import os
import random
import smtplib

engine  = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour < 16:
        speak("Good afternoon!")
    elif hour >= 16 and hour <20:
        speak("Good evening!")
    else:
        speak("Good Night!")
    
    speak("I'm Friday. How can I help you?")

def takeCommand():
    # takes microphone input from user and returns
    # string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = 100
        audio = r.listen(source)
    
    try:
        #print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Come again...")
        return "none"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('odinson947@gmail.com', '**************')
    server.sendmail('kakaricardo771@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    #speak("James Hetfield")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        if 'open youtube' in query:
            webbrowser.open('youtube.com')

        if 'play music' in query:
            folder = 'X:\\Stolen Music\\The Top 500 Heavy Metal Songs of All Time'
            songs =  os.listdir(folder)
            print(songs)
            os.startfile(os.path.join(folder, songs[random.randrange(0, 200)]))

        if 'time' in query:
            t = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {t}")

        if 'sublime text' in query:
            path = 'X:\\Program Files\\Sublime Text 3\\sublime_text.exe'
            os.startfile(path)

        if 'email to me' in query:
            try:
                speak('what should I say')
                content = takeCommand()
                to = 'kakaricardo771@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('sorry sir. I am not able to send this email')


        if 'bye' in query:
            speak('Pleased to help you sir.')
            break;        

















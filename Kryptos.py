import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random 
import smtplib 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Kryptos! Please tell me how may I help you?")

def takeCommand():
    '''
        It takes microphone input from the user and returns string output
    
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    # print(type(audio))
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
    
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('your_email_here', 'your_password')
    server.sendmail('your_email_here', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic based on task on query
        if 'wikipedia' in query:
            speak("Searching Wikepedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Audio\\Raps'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,3)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir! The time is {strTime}")
        elif 'open code' in query:
            os.startfile("C:\\Users\\shoai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            speak("opening Visual studio Code")
        elif 'exit' == query:
            break
        elif 'who are you' or 'your name' in query:
            speak("I am Kryptos. Your's personal voice assistant")
        elif 'email to FRIEND_NAME' in query: # you can add as many friends as you want
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "EMAIL_OF_FRIEND"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Shoaib! I am not able to send this email.")
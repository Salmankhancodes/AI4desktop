import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour=datetime.datetime.now().hour
    if hour>0 and hour<12:
        speak("Good morning Sir")
    elif hour > 12 and hour<17:
        speak("Good after noon sir")
    else:
        speak("Good evening sir")
    speak("I am your assistant. HOW may i help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language='en-in')
        print(f"You said : {query}")
    except Exception as e:
        print("Sorry can't recognize your voice")

    return query

def sendEmail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('enter you email id here','enter your password here')
    server.sendmail('(to whom you want to send) mail id',to,content)
    server.close()

if __name__ == '__main__':
        greetings()
        while True:
            query = takeCommand().lower()
            speak(f"you said:: {query}")
            if 'the time' in query:
                tm=datetime.datetime.now().strftime("%H:%M:%S")
                print(f"the time is {tm}")
                speak(f"the time is {tm}")
            elif 'wikipedia' in query:
                print("Searching wikipedia")
                speak("Searching wikipedia")
                query=query.replace("wikipedia","")
                result=wikipedia.summary(query,sentences=2)
                print(result)
                speak(f"According to wikipedia...{result}")
                speak(result)

            elif 'google' in query:
                webbrowser.open("google.com")

            elif 'youtube' in query:
                webbrowser.open("youtube.com")

            elif 'play music' in query:
                musicdir="E:\\mp3"
                songs=os.listdir(musicdir)
                os.startfile(os.path.join(musicdir,songs[0]))

            elif 'open code' in query:
                path="path of your directory"
                os.startfile(path)
            elif 'email' in query:
                try:
                    speak("Enter your email id")
                    to=input("Enter email id")
                    speak("what should i say ?")
                    content= takeCommand()
                    sendEmail(to,content)
                    speak("Email sent successfully")
                    print("Sent Successfully!!")
                except:
                    speak("Sorry email cannot be sent due to some error occured")
                    print("Email sending failed")
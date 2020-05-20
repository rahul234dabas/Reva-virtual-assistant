import pyttsx3 #before installing this make sure to be in your native coding envirnoment and not in virtual envirnoment ...... pip install pywin32 and pyaudio is must
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir!')
    elif ( hour>=12 and hour < 17 ):
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')
    speak('Hi! I am Reva. How may I help you?')
def takecommand():
    # takes microphone input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print('Recognizing..')
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("Please Say that again....")
        return  "None"
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremailid@gmail.com","yourpasswrd")#your email id and passwrd
    server.sendmail('rahul234dabas@gmail.com',to ,content)#your mail id
    server.close()


if __name__ == '__main__':
    welcome()
    while(True):
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("Searchin Wikipedia")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            speak(results)
        elif'open youtube' in query:
            webbrowser.open("youtube.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            music_file="C:\\Users\\rahul\\Music\\sweet"
            songs=os.listdir(music_file)
            print(songs)
            os.startfile(os.path.join(music_file,songs[0]))
        elif "time" in query:
            time_now=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir the time is {time_now}")
        elif "good girl" in query:
            speak("yes daddy!!")
        elif "open code" in query:
            py_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
            os.startfile(py_path)
        elif "what\'s up" in query or 'how are you' in query:
            options = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','ek dum maastt!']
            speak(random.choice(options))
        elif "i love you" in query:
            speak("soory,i have a boyfriend!! sir")
        elif "send email" in query:
            try:
                speak("what should I say?")
                content = takecommand()
                to = "shubhamanand98@outlook.com" #emailid to which you want to send mail
                sendemail(to,content)
                speak("Sir, email has been sent!!")
            except Exception as e:
                print(e)
                speak("sorry sir I am not able to send the email")








#pYttsx3 is a library we use microsoft Speech API 5 to convert text to speech
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os #operating system
import random
import smtplib #simple mail transfer protocal
from plyer import notification

mail_dictionary = {}
def add_mail(name,email):
    mail_dictionary[name]=email
def get_mail(name):
    if name in mail_dictionary:
        return mail_dictionary[name]
    else:
        return "Mail not found"
add_mail("example1","example1@gmail.com")
add_mail("example2","example2@gmail.com")
add_mail("example3","example3@gmail.com ")

#sapi5 is the driver
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak('do you want the voice to be of Rahul or Lily? ')
    query1 = takeCommand().lower()
    
    if 'rahul' in query1:
        name="Rahul"
        engine.setProperty('voice',voices[0].id)
        
    elif 'lily' in query1:
        name="Lily"
        engine.setProperty('voice',voices[1].id)

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, Myself"+ name +". Please tell me how can i help you? ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Myself"+ name +". Please tell me how can i help you? ")
    else:
        speak("Good evening, Myself"+ name +". Please tell me how can i help you? ")
    
def takeCommand():
    #it takes microphone input from the user and returns string inputs
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1;
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"   
    return query 

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    print('trying to log in')
    server.login('example@gmail.com','your_pass(16 digit)')
    print('login success')
    server.sendmail('example@gmail.com',to,content)
    server.close()

if __name__ == "__main__":

    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open whatsapp web' in query:
            webbrowser.open("whatsapp.com")
        elif 'open telegram web' in query:
            webbrowser.open("telegram.org")
        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.org")
        elif 'open chat gpt' in query:
            webbrowser.open("https://openai.com/blog/chatgpt")
        elif 'play music' in query:
            speak('do you want me to play a random music')
            answer=takeCommand().lower()
            if 'yes' in answer:
                music_dir = 'C:\\Users\\HP\\Desktop\\music'
                songs = os.listdir(music_dir)
                print(songs)
                i=random.randint(0,len(songs)-1)
                print(i)
                os.startfile(os.path.join(music_dir,songs[i]))
            elif 'no' in answer:
                speak('Let me know the song')
                songtoplay=input().lower()
                music_dir = 'C:\\Users\\HP\\Desktop\\music'
                songs = os.listdir(music_dir)
                print(songs)
                for i in (0,len(songs)-1):
                    if songs[i].lower()==songtoplay:
                        os.startfile(os.path.join(music_dir,songs[i]))
                        break
                    else:
                        speak('song not found')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")
            print(strDate)
            speak(strDate)
        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak('whom do you want to send the mail? ')
                reciever=takeCommand()
                speak("what should I say?")
                content = takeCommand()
                to = get_mail(reciever)
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the mail")
        
        
        elif 'end chat' in query:
            break
        



import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import operator
from translate import Translator
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import winsound
from win10toast import ToastNotifier
import pyautogui
import time


df = pd.read_csv('iphone_price.csv')
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
def get_operator_fn(op):
    return{
        '+' : operator.add,
        '-' : operator.sub,
        'into' : operator.mul,
        'multiply by':operator.mul,
        'divided' : operator.__truediv__,
        'by' : operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
    }[op]

def eval_binary_expr(op1,oper,op2):
    op1,op2 = int(op1),int(op2)
    return get_operator_fn(oper)(op1,op2)
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)   
    if hour>=0 and hour<12:
        talk('Good Morning Sir! Katto here! How can I help you')
    elif hour>=12 and hour <18:
        talk('Good Afternoon Sir! Katto here! How can I help you')
    else:
        talk('Good Evening Sir! Katto here! How can I help you') 
wishme()          
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            talk("Listening")
            voice = listener.listen(source)         #Using microphone to listen up as source
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                #talk(command)

    except:
        pass

    return command

def run_Alexa():
    command = take_command()
    #print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing'+song)
        pywhatkit.playonyt(song)  
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        talk(f"Time is {time}")   
    elif 'google' in command:
        webbrowser.get('chrome').open('google.com')
    elif 'facebook' in command:
        webbrowser.get('chrome').open('facebook.com')
    elif 'instagram' in command:
        webbrowser.get('chrome').open('instagram.com')
    elif 'whatsapp' in command:
        webbrowser.get('chrome').open('web.whatsapp.com')
    elif 'personal' in command:
        webbrowser.get('chrome').open('https://mail.google.com/mail/u/0/#inbox')
    elif 'college' in command:
        webbrowser.get('chrome').open('https://mail.google.com/mail/u/1/#inbox')
    elif 'linkedin' in command:
        webbrowser.get('chrome').open('https://www.linkedin.com/in/raghav-mishra-b350b6174/')    
    elif 'wikipedia' in command:
        person = command.replace('wikipedia','')
        info = wikipedia.summary(person,3)
        talk(info)   

    elif 'wiki' in command:
        person = command.replace('wikipedia','')
        info = wikipedia.summary(person,3)
        talk(info)   
    elif 'who is' in command:
        person = command.replace('wikipedia','')
        info = wikipedia.summary(person,3)
        talk(info)      
    elif 'joke' in command:
        talk('OK thats Interesting')
        talk('So here is the joke')
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke()) 
    elif 'calculate' in command:
        string = command.replace('calculate','')
        #print(*(string.split()))
        talk(eval_binary_expr(*(string.split()))) 
    elif 'price' in command:
        no = command.replace('price','')
        so = no.replace('of','')
        po = so.replace('iphone','')
        model = LinearRegression()
        model.fit(df[['version']],df[['price']])
        a = int(po)
        talk(model.predict([[a]]))
        talk('dollar')
        print('Iphone'+po)
        print(model.predict([[a]]))   
        print('dollar')

    elif 'translate' in command:
        print(command)
        if 'hindi' in command:
            text = command.replace('translate','')
            text = command.replace('hindi','')
            translator= Translator(to_lang="hi")
            translation = translator.translate(text)
            print(translation)
            talk(translation)
        elif 'spanish' in command:
            text = command.replace('translate','')
            text = command.replace('spanish','')
            translator= Translator(to_lang="es")
            translation = translator.translate(text)
            print(translation)
            talk(translation)
        elif 'chinese' in command:
            text = command.replace('translate','')
            text = command.replace('chinese','')
            translator= Translator(to_lang="zh")
            translation = translator.translate(text)
            print(translation)
            talk(translation)  
        elif 'portuguese' in command:
            text = command.replace('translate','')
            text = command.replace('portuguese','')
            translator= Translator(to_lang="pt")
            translation = translator.translate(text)
            print(translation)
            talk(translation)           
    elif 'search' in command:
        search = command.replace('search','')
        webbrowser.get('chrome').open('https://www.google.com/search?q='+search)   
    elif 'alarm' in command:
        def timer(reminder,time):
            notificator=ToastNotifier()
            notificator.show_toast("Remainder",f"Alarm will go off in (time) minutes",duration=20)
            notificator.show_toast(f"Reminder",reminder,duration=20)
            # Alarm
            frequency=250
            duration=1000
            winsound.Beep(frequency,duration)
        talk('What would you be remind of')
        words = input('What would you be remind of: ')    
        talk('Enter time in minutes')
        sec = input('Enter time in minutes:')*60
        timer(words,sec)  
    elif 'spam' in command:
        talk('Enter the text you want to spam')
        spam_text = input('Enter the text to spam: ')
        talk('Enter how many time you want to spam')
        count=input('Enter how many time you want to spam: ')
        talk('Move the cursor where you want to spam')
        time.sleep(5)
        for _ in range(count):
            pyautogui.typewrite(spam_text)
            pyautogui.press('enter')
            time.sleep(1)         
    elif 'exit' in command:
        talk('Bye! Sir! have a nice day')
        exit()       
    else:
        talk('Sorry!Please say that again')             
while True:
    run_Alexa()        
"""
A basic program to use speech recognition and wikipedia search libraries

Author: Akash TP

Date: 10/04/2021

"""
import SpeechRecognition  as sr
import os
import datetime
from gtts import gTTS
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

#Methode to record audio and return it as a string
def recordAudio():
    r = sr.Recogniser()
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said "+ data)
    except sr.UnknownValueError:
        print("Sorry I didn't catch that!")
    except sr.RequestError as e:
        print("Request error from google Speech recognition")
    return data

#Methode to get assistant response
def assistantResponse(text):
    print(text)
    #Convert the text to speech
    obj = gTTS(text = text, lang = 'en', slow = False)
    #Save the converted audio to a file
    obj.save("assistant_response.mp3")
    #Play the converted file
    os.system('start assistant_response.mp3')

#Method to wake assistant
def wake(text):    
    WAKE_WORDS = ['hey jarvis', 'jarvis']
    text = text.lower()
    for phrases in WAKE_WORDS:
        if phrases in text:
            return True
    return False

#Method to get the date
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    month = now.month
    daynum = now.day

    month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', 
                      '7th', '8th', '9th', '10th', '11th', '12th',                      
                      '13th', '14th', '15th', '16th', '17th', 
                      '18th', '19th', '20th', '21st', '22nd', 
                      '23rd', '24th', '25th', '26th', '27th', 
                      '28th', '29th', '30th', '31st']
    return "Today is " + weekday + " " +  month_name[month - 1] +"the " + ordinalNumbers[daynum - 1] + "."

#Method to return greeting response
def greeting(text):
    INPUTS = ["hi", "Hello", "wazzzzup"]
    RESPONSES = ["Hey there", "Howdy partner", "wassup my nigga"]

    for word in text.split():
        if word.tolower() in INPUTS:
            return random.choice(RESPONSES) + "."
    return ""

#Method to get the user's name
def getPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i+3 <= len(wordList) - 1 and wordList[i].tolower() == 'who' and wordList[i+1].tolower() == 'is':
            return wordList[i+2] + ' ' + wordList[i+3]

while True:
    # Record the audio
    text = recordAudio()
    response = '' #Empty response string
     
    # Checking for the wake word/phrase
    if (wakeWord(text) == True):
         # Check for greetings by the user
        response = response + greeting(text)
         # Check to see if the user said date
        if ('date' in text):
            get_date = getDate()
            response = response + ' ' + get_date
         # Check to see if the user said time
        if('time' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m' #Post Meridiem (PM)
                hour = now.hour - 12
            else:
                meridiem = 'a.m'#Ante Meridiem (AM)
                hour = now.hour
           # Convert minute into a proper string
            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)
            response = response + ' '+ 'It is '+ str(hour)+ ':'+minute+' '+meridiem+' .'
                
        # Check to see if the user said 'who is'
        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)            
            response = response + ' ' + wiki
       
       # Assistant Audio Response
    assistantResponse(response)
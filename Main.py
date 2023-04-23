import cv2
from simple_facerec import SimpleFacerec
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
import os
import sys
import subprocess

sfr = SimpleFacerec()
sfr.load_encoding_images("Add the dataset images path here")

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate",150)
engine.setProperty('voice', voices[1].id)
global command
ace=""
hrmin=datetime.datetime.now()

cap = cv2.VideoCapture(0)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def runalexa():
    global command
    command = ''
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'what is' in command:
        data = command.replace('what is ', '')
        info = wikipedia.summary(data,5)
        print(info)
        talk(info)
    elif 'where is' in command:
        data = command.replace('where is', '')
        info = wikipedia.geosearch(data,5)
        print(info)
        talk(info)
    elif 'which' in command:
        data = command.replace('which', '')
        info = wikipedia.summary(data,5)
        print(info)
        talk(info)
    elif 'okay thank you' in command:
        subprocess.call([sys.executable,os.path.realpath(__file__)]+sys.argv[1:])
while True:
    ret, frame = cap.read()
    cv2.imwrite("image.png", frame)

    face_locations,face_names=sfr.detect_known_faces(frame)
    for face_loc,name in zip(face_locations,face_names):
        y1, x2,y2,x1=face_loc[0],face_loc[1],face_loc[2],face_loc[3]
        ace = name
        cv2.putText(frame,name,(x1,y1 -10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,200),2)
        cv2.rectangle(frame,(x1, y1),(x2,y2),(0,0,200),4)
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
    if ace=="keertha":
        break
    elif ace=="Unknown":
        pywhatkit.sendwhats_image("Add a whatsapp Number with the country code","Add the path of the image which is added to the current folder","Detected The Unknown Face",20)
        break
    

cap.release()
cv2.destroyAllWindows()

while name=="keertha":
    runalexa()

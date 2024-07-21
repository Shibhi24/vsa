import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises...Please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything..')
        recordedaudio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(recordedaudio)
            command = command.lower()
            print('You said: ' + command)
            if 'search' in command:
                webbrowser.open('(link unavailable)' + command.replace('search', ''))
            elif 'play' in command:
                pywhatkit.playonyt(command.replace('play', ''))
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)
                engine.say(time)
                engine.runAndWait()
            else:
                print('Sorry, I didn\'t understand that.')
                engine.say('Sorry, I didn\'t understand that.')
                engine.runAndWait()
        except Exception as e:
            print('Sorry, I didn\'t understand that.')
            engine.say('Sorry, I didn\'t understand that.')
            engine.runAndWait()

cmd()
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
# import numpy

engine = pyttsx3.init()

def talk(voice):
    engine.say(voice)
    engine.runAndWait()

print("hello")

listener = sr.Recognizer()

def take_command():

    try:
        with sr.Microphone() as source:
            print('listening')
            listener.adjust_for_ambient_noise(source, duration=0.5)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
            else:
                print('Alexa: You missed my name')
            
    except:
        print("Sorry, voice not recognized :(")
        pass

    return command

def run_alexa():

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    # elif 'bye' in command:
    #     talk('Bye, see you again!')
    #     break

    else:
        talk('Please say the command again.')

while True:
    command = take_command()
    run_alexa()
    if 'bye' in command:
        talk('Bye, see you again!')
        break

print("hell 2")
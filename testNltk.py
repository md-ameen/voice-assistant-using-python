import re
from tkinter import *
# from nltk.chat.util import Chat, reflections
from pairs import my_pairs
# from alexa import alexa
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import numpy

root = Tk()
root.title("CHAT BOT")
# root.geometry('300x300')

txt = Text(root, width=40, font='Verdana', fg='white', bg='#E23A3A')
txt.grid(row=0, column=0, columnspan=8)

e = Entry(root, width=50, fg='black',  borderwidth=0)
e.grid(row=1, column=0, ipady=10, pady=5)
e.insert(0, "Type a message")

txt.insert(END, "Welcome to the Chat Bot. Start Chatting Now! ")

engine = pyttsx3.init()


def talk(voice):
    engine.say(voice)
    engine.runAndWait()
    # newVoiceRate =5000
    # engine.setProperty('rate',newVoiceRate)


listener = sr.Recognizer()


def send():

    send = "You: " + e.get()
    txt.insert(END, "\n" + send)

    if re.findall(my_pairs[0], e.get()):
        matchObj = re.findall(my_pairs[0], e.get())
        txt.insert(END, "\n" + "Bot: Hi " + ''.join(matchObj))

    elif re.findall(r"hi (.*)", e.get()):
        matchObj = re.findall(r"hi (.*)", e.get())
        txt.insert(END, "\n" + "Bot: Hi I am " + ''.join(matchObj))

    elif re.findall(r"weather in (.*)", e.get()):
        matchObj = re.findall(r"weather in (.*)", e.get())
        txt.insert(END, "\n" + "Bot: The weather in " +
                   ''.join(matchObj) + ' is amazing always')
        talk("The weather in " + ''.join(matchObj) + ' is amazing always')

    elif re.findall(r"hi|hello|hey", e.get()):
        txt.insert(END, "\n" + "Bot: Hi There ", 'color')
        txt.tag_configure('color', background="black", foreground="red")
        talk('Hi there')

    elif re.findall(r"(.*) location|city|living", e.get()):
        txt.insert(END, "\n" + "Bot: India ")
        talk('Bot: India')

    elif re.findall(r"how are you\??", e.get()):
        txt.insert(END, "\n" + "Bot: I am fine ")

    elif re.findall(r"(.*) created you", e.get()):
        txt.insert(END, "\n" + "Bot: Ameen did using Tkinter ")
        talk('Ameen did using Tkinter')

    elif re.findall(r"your name", e.get()):
        txt.insert(END, "\n" + "Bot: My name is A.L.E.X.A")
        talk("My name is alexa")

    elif re.findall(r"help", e.get()):
        txt.insert(END, "\n" + "Bot: I can help you :) ")

    else:
        txt.insert(END, "\n" + "Bot: Sorry This kind of regex not included :(")

    e.delete(0, END)


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening')
            listener.adjust_for_ambient_noise(source, duration=0.5)
            voice = listener.listen(source)
            print('listening2')
            command = listener.recognize_google(voice)
            print('listening3')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        print("Sorry, voice not recognized :(")
        pass

    return command


def voice_chat():
    voice_op = take_command()
    txt.insert(END, "\n" + "You: " + voice_op)

    if re.findall(r"how are you\??", voice_op):
        x = txt.insert(END, "\n" + "Bot: I am fine ")
        talk('I am fine')

    elif 'play' in voice_op:
        song = voice_op.replace('play', '')
        txt.insert(END, "\n" + "Bot: Playing " + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in voice_op:
        time = datetime.datetime.now().strftime('%I:%M %p')
        txt.insert(END, "\n" + "Bot: " + time)
        talk('Current time is '+time)

    elif 'who is' in voice_op:
        person = voice_op.replace('who is', '')
        info = wikipedia.summary(person, 1)
        txt.insert(END, "\n" + "Bot: " + info)
        talk(info)

    elif 'joke' in voice_op:
        joke = pyjokes.get_joke()
        txt.insert(END, "\n" + "Bot: " + joke)
        talk(joke)

    elif 'bye' in voice_op:
        talk('Bye, see you again!')
        # break

    # else:
    #     talk('Please say the command again.')

    else:
        txt.insert(END, "\n" + "Bot: This regex not included :(")


my_dummy_reflections = {
    'go': 'gone',
    'hello': 'hey there!'
}

# chat = Chat(pairs, my_dummy_reflections)

send_img = PhotoImage(file='C:/Users/ameen/Desktop/NLTK/send button.png')
# img_label = Label(image = send_img)
# send_img = send_img.zoom(4)
send_img = send_img.subsample(20)

voice_img = PhotoImage(file='microphone-3404243_1280.png')
voice_img = voice_img.subsample(40)

send_btn = Button(root, image=send_img, command=send, borderwidth=0)
send_btn.grid(row=1, column=1, padx=15)

voice_btn = Button(root, image=voice_img, command=voice_chat, borderwidth=0)
voice_btn.grid(row=1, column=2)

# chat.converse()

root.mainloop()

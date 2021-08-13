import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.7)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# text.set(engine=text.TexEngine, texmessages_end=[text.texmessage.ignore])

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
    except:
        pass
    return command
def take_command_of_message():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'go for a date' in command:
        talk('sorry, i am not interested')
    elif 'are you single' in command:
        talk('no i am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'send whatsapp message' in command:
        talk("tell me the number on which you want to send message")
        number = take_command()
        phonenumber = '+91' + number
        talk("tell me the message which you want to send")
        message = take_command_of_message()
        talk("tell me the at what time you want to send the message, in hours")
        hour = take_command_of_message()
        talk("tell me the minute now")
        minute = take_command_of_message()
        pywhatkit.sendwhatmsg(phonenumber, message, hour, minute)
    else:
        talk('please speak again')
while True:
    run_alexa()
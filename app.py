#import pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if("alexa" in command):
                command.replace("alexa", "")
                return command             
                
    except:
        command = "erro"

    return command
    
    
def run_alexa():
    command = take_command()

    if("play" in command):
        song = command.replace("play", "")
        talk("ok, playing " + song)
        pywhatkit.playonyt(song)
    elif("time" in command):
        time = datetime.datetime.now().strftime("%H:%M %p")
        talk("current time is " + time)
    elif("what is" in command):
        command = command.replace("what is", "")
        talk("i'm searching for " + command + ".")
        info = wikipedia.summary(command, 1)
        talk(info)
    elif("date" in command):
        talk("sorry, i have a headache")
    elif("are you single" in command):
        talk("no, i am in a relationship with your wifi.")
    elif("joke" in command):
        talk("yes shure. " + pyjokes.get_joke())


while True:
    run_alexa()

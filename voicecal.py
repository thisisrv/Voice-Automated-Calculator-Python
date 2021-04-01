import pyttsx3
import speech_recognition as sr
import operator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    
r = sr.Recognizer()
my_mic_device = sr.Microphone(device_index=1)

speak("Hello sir!! This is female Jarvis")
with my_mic_device as source:
    speak("What you want me to calculate sir? example: 3 plus 3")
    print("Listening...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
my_string=r.recognize_google(audio)

print('Sir: ' + my_string)

def get_operator(op):
    return{
           '+' : operator.add,
           '-' : operator.sub,
           'x' : operator.mul,
           'X' : operator.mul,
           'divided' : operator.__truediv__,
           'Mod' : operator.mod,
           'mod' : operator.mod,
            }[op]
    
def eval_binary_expr(op1, opr, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator(opr)(op1, op2)

speak('Sir!! The result is :')

c=eval_binary_expr(*(my_string.split()))
speak(str(c))
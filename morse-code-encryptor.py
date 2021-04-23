import RPi.GPIO as GPIO
import time
import pdb

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
ledPin = 12
GPIO.setup(ledPin, GPIO.OUT)

def dot():
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(2.0)
    GPIO.output(ledPin, GPIO.LOW)
    
def dash():
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(4.0)
    GPIO.output(ledPin, GPIO.LOW)
    
code = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }
    


def encrypt_message():
    message = input ("What would you like to encode?")
    message = message.lower()
    for x in message:
        letter = code.get(x)
        if letter:
            for y in letter:          
                if y == ".":
                    dot()
                elif y == "-":
                    dash()
        elif x == " ":        
            time.sleep(8.0)
    encrypt_message()
    
    
encrypt_message()

import cowsay
import pyttsx3

engine = pyttsx3.init("nsss")
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
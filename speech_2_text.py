from flask import Flask
app = Flask(__name__)
from gtts import gTTS
import os 

import speech_recognition as sr 
# @app.route("/getspeech_to_text", methods = ["POST"])
def speech_to_text():
	#Recognizer class
	#Create an instance for Recognizer class
	r = sr.Recognizer()
	#Each Recognizer instance has methods for recognizing speech from an audio source using various APIs
	while True:
		with sr.Microphone() as source:
			print("Speak Anything..: ")
			r.adjust_for_ambient_noise(source, duration =1)
			audio = r.listen(source)
			# print('Audio',audio)
		try:
			text = r.recognize_google(audio)
			text_to_speech(text)
			print("you said: " +text)
		except Exception as e:
			return (e)
def text_to_speech(text):
	tts = gTTS(text=text, lang='en')
	tts.save("audio2.mp3")
	os.system('mpg321 audio2.mp3 -quiet')
# app.run(host = "192.168.5.180", port = 5001)
text = speech_to_text()

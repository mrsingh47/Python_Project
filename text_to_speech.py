"""WAP to convert text to speech"""
import gtts
import os
myspeech = gtts.gTTS(text="Hello, My name is BHAVYA PRATAP SINGH", lang='en',slow='false')
myspeech.save("myspeech.mp3")
os.system("myspeech.mp3")
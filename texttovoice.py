#!pip install gtts
from gtts import gTTS           #google text to speech library
#!pip install playsound
from playsound import playsound		#playsound module to save and playing audio
audio='texttoaudios.mp3'			#name for the audio file 
language ='en'						#language of text
f=open("sample3.txt","r")			#opening text file 
texts=f.read()						#reading text from text file				

f.close()
sp=gTTS(text=texts,lang=language,slow=False)			#text, language of text and speed of speech
sp.save(audio)					#saving the audio
playsound(audio)				#playing sound
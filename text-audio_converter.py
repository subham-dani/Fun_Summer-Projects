from gtts import gTTS
from playsound import playsound
audio = 'speech-new.mp3'
language ='en'

sp = gTTS(text='Fucking khanna why are you sleeping',lang=language,slow=False)

sp.save(audio)
playsound(audio)
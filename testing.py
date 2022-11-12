from gtts import gTTS
import os    

tts = gTTS(text="This is the pc speaking", lang='en')
tts.save("pcv.mp3")
# to start the file from python

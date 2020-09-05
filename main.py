from gtts import gTTS
import os
f=open('texttoread.txt')
file=f.read()
language='en'
audio=gTTS(text=file,lang=language,slow=False)
audio.save("texttoread.wav")
os.system("texttoread.wav")
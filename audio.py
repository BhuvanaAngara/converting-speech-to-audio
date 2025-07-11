from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = 'en'
sp = gTTS(text = "my name is bhuvana angara and this is my python project",
          lang = language,
          slow = False)
sp.save(audio)
playsound(audio)
print("=====audio is playing=====")

import os
import shutil
import playsound3
from gtts import gTTS
from pathlib import Path
from funcionalidades.control_rutas import ruta

def speak(text):
    tts = gTTS(text=text, lang='en',slow=False)
    filename ='speech.mp3'
    tts.save(filename)
    playsound3.playsound(filename)
    
def speakChiste(chiste):
    
    tts = gTTS(text=chiste, lang='en',slow=False)
    file ='chiste.mp3'
    mpDir=Path(f"{ruta()}/{file}")
    rVozx=Path(f"{ruta()}/DBChuck_audio")
    tts.save(file)
    playsound3.playsound(file) 
    initial_count = 0
    dir = rVozx
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            initial_count += 1
    initial_count= initial_count+1
    file=f'{initial_count}_{file}'
    rVoz=Path(f"{ruta()}/DBChuck_audio/{file}")
    shutil.move(f'{mpDir}', f'{rVoz}')
    print(initial_count)
    
def habla(text):
    tts = gTTS(text=text, lang='es',slow=False)
    filename ='speech.mp3'
    tts.save(filename)
    playsound3.playsound(filename) 
   
    

speak("""  Hello and wellcome!
       I will be your assistant during this session, 
       my name is Claris, former C I A  agent, with a bad temper
       a gun and very little time to lose   
       enjoy....Grrrrrr the jokes and hurra """)
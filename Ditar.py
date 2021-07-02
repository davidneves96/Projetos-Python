
import speech_recognition as sr 
import pyautogui as p
import pyperclip as py
import time as t


r = sr.Recognizer()

mic = sr.Microphone();

x = 0

t.sleep (3)

while x == 0:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        saida = r.recognize_google(audio, language = 'pt-BR')
       
        if saida == ("parar"):
            x = 1
            p.write ("parando de escrever com python")
        else:
            py.copy (saida)
            p.hotkey ("ctrl", "v")
        p.press ("enter")
        

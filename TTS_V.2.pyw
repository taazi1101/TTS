from tkinter import *
import os
import sys
import subprocess

try:
    from gtts import gTTS
    from playsound import playsound
except ImportError as e:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gtts"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "playsound"])
    from gtts import gTTS
    from playsound import playsound

root = Tk()
root.title("Text To Speech")
root.resizable(False, False)

text_box = Text(height=20, width=100)
lang_entry = Entry(width=4)
text_box.grid(row=1, column=0, columnspan=3)
lang_entry.grid(row=3, column=2)
lang_entry.insert(0, 'en')

isslow = False
def text_to_speech():
    global mp3name
    Message = str(text_box.get(1.0, END))
    listofwords = str(text_box.get(1.0, END)).split()
    mp3name = listofwords[0] + '_TTS.mp3'
    if 'ä' in listofwords[0] or 'Ä' in listofwords[0]:
        mp3name = 'fn_TTS.mp3'
    speech = gTTS(text=Message,lang=str(lang_entry.get()),slow=isslow)
    if len(mp3name) > 20:
        mp3name = Message[1:15] + '_TTS.mp3'
    speech.save(mp3name)

def slowmode():
    global isslow
    if isslow == True:
        isslow = False
        slow_button = Button(text="Slow\nMode", padx=115, pady=3, command=slowmode)
        slow_button.grid(row=2, column=1)
        return
    if isslow == False:
        isslow = True
        slow_button = Button(text="Slow\nMode", bg='green', padx=115, pady=3, command=slowmode)
        slow_button.grid(row=2, column=1)
        return

def delete():
    os.remove(mp3name)

def play():
    Message = str(text_box.get(1.0, END))
    playmp3 = 'c:/temp/TTS_PLAY.mp3'
    speech = gTTS(text=Message,lang=str(lang_entry.get()),slow=isslow)
    speech.save(playmp3)
    playsound(playmp3)
    os.remove(playmp3)

slow_button = Button(text="Slow\nMode", padx=115, pady=3, command=slowmode)
convert_button = Button(text="Generate", padx=243, pady=10, command=text_to_speech)
delete_button = Button(text="Delete", padx=115, pady=10, command=delete)
play_button = Button(text="Play", padx=115, pady=10, command=play)

delete_button.grid(row=2, column=0)
play_button.grid(row=2, column=2)
slow_button.grid(row=2, column=1)
convert_button.grid(row=3, column=0, columnspan=2)

root.mainloop()

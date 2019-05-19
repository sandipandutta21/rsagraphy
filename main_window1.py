from tkinter.ttk import *
from tkinter import *
import sys
import os
import subprocess

main_window = Tk()
main_window.geometry( '430x300' )
main_window.title( 'RSAGRAPHY' )

lbl1 = Label(main_window, text = "                          Encryptor", font= ( 'Arial, Bold', 15 ) ) #TODO bind everything with .bind()
lbl1.place( x=10, y=10 )

def text():
        subprocess.check_call(["python3", "text1copy.py"])

def image():
        subprocess.check_call(["python3", "image1copy.py"])

def video():
        subprocess.check_call(["python3", "video.py"])

def audio():
        subprocess.check_call(["python3", "audio1copy.py"])

def close():
	exit()

def keygen():
	 subprocess.check_call(["python3", "rsa1copy.py"])

btn_key = Button( main_window, text = "KEY GENERATION", command = keygen )
btn_key.place( x=140, y=90 )

btn_text = Button( main_window, text = "Text", command = text )
btn_text.place( x=50, y=140 )

btn_image = Button( main_window, text = "Image", command = image )
btn_image.place( x=130, y=140 )

btn_audio = Button( main_window, text = "Audio", command = audio )
btn_audio.place( x=220, y=140 )

btn_video = Button( main_window, text = "Video", command = video )
btn_video.place( x=310, y=140 )

btn_exit = Button( main_window, text = "Exit", command = close)
btn_exit.place( x=140, y=200 )

btn_help = Button( main_window, text = "HELP", command = close)
btn_help.place( x=210, y=200 )

main_window.mainloop()

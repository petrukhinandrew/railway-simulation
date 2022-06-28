from tkinter import *
from tkinter import ttk
import random

#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("750x250")

def change_style():
   label.config(font=('Impact', 15 ,'italic'), foreground= "white", background="black")
   button.config(text= "Close", command=lambda:win.destroy())

#Create a Canvas
canvas= Canvas(win, width= 600, height=200, bg='bisque')
canvas.pack(fill= BOTH, expand= True)

#Create a Label
label=Label(canvas, text= "Welcome to TutorialsPoint.com", font=(None, 15))
label.pack(pady=14)
#Create a button in canvas
button= Button(canvas, text="Click Me", command= change_style)
button.pack(pady=20)

win.mainloop()
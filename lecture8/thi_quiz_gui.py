# -*- coding: utf-8 -*-
"""
thi_quiz_gui.py

A tkinter GUI with the quiz_logo.png, a label for the question,
2 x 2 buttons for the answers. Start with a mockup example

Created on Tue Nov 23 22:27:53 2021

@author: 
"""
import tkinter
from pathlib import Path 

root = tkinter.Tk()
root.title("Quiz")
canvas = tkinter.Canvas(root)
canvas.grid(row=0, column=0, rowspan=4, columnspan=2)
#root.geometry("400x300")

# Load the quiz logo
quiz_logo_path = Path(__file__).with_name("quiz_logo.png")
logo = tkinter.PhotoImage(file=quiz_logo_path)
logo_label = tkinter.Label(root, image=logo)
logo_label.grid(row=0, column=0, columnspan=2)

# Create a label for the question
question_label = tkinter.Label(root, text="What is the capital of France?")
question_label.grid(row=1, column=0, columnspan=2)

# Create buttons for the answers
button1 = tkinter.Button(root, text="Berlin")
button1.grid(row=2, column=0)

button2 = tkinter.Button(root, text="Madrid")
button2.grid(row=2, column=1)

button3 = tkinter.Button(root, text="Paris")
button3.grid(row=3, column=0)

button4 = tkinter.Button(root, text="Rome")
button4.grid(row=3, column=1)

root.mainloop()

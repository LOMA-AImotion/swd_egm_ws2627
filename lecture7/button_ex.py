import tkinter
from tkinter import messagebox # some weird error with tkinter
import webbrowser

def say_hi():
    print("Hello EGM")
    messagebox.showerror("Hi EGM", "Hello to tkinter")
    webbrowser.open(text_input.get("1.0", "end-1c")) # get the text from the text box and open it in a browser

main_win = tkinter.Tk()
text_input = tkinter.Text(main_win, height=5, width=30)
text_input.pack()
btn = tkinter.Button(main_win, text="Say hi", command=say_hi)
btn.configure(command=say_hi) # could have been done in the button creation
btn.pack()

main_win.mainloop()
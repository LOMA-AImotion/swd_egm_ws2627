import tkinter

main_win = tkinter.Tk()
main_win.title("THI - EGM - SWD")

label = tkinter.Label(main_win, text="This is my first GUI")
label.grid(row=0, column=0)

button = tkinter.Button(main_win, text="OK")
button.grid(row=1, column=1)
main_win.mainloop()
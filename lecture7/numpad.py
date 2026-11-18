import tkinter
main_window = tkinter.Tk()
main_window.title("EGM SWD Numpad")

counter = 1
for row in range(3):
    for col in range(3):
        new_button = tkinter.Button(main_window, text=counter, height=5, width=10, bg="green")
        new_button.configure(fg="white")
        new_button.grid(row = row, column=col)
        counter = counter + 1
main_window.mainloop()
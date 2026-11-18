import tkinter

main_window = tkinter.Tk()
canvas = tkinter.Canvas(main_window, width=600, height=400)

canvas.grid(row=0, column=0, rowspan=2, columnspan=4)
main_window.mainloop()
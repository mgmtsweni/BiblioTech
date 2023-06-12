from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#f36424")
canvas = Canvas(
    window,
    bg = "#f36424",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file="img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = -526, y = 261,
    width = 356,
    height = 84)

img1 = PhotoImage(file="img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = -529, y = 103,
    width = 356,
    height = 84)

canvas.create_text(
    -362.0, -45.5,
    text = "Library In Your Pocket",
    fill = "#ffffff",
    font = ("None", int(54.0)))

window.resizable(False, False)
window.mainloop()

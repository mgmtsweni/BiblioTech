from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1526x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1526,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    -1125.0, 170.0,
    text = "Forgot Password?",
    fill = "#7b13c3",
    font = ("Inter-Bold", int(32.0)))

canvas.create_text(
    -808.0, 170.0,
    text = "Click here",
    fill = "#f36424",
    font = ("Inter-Bold", int(32.0)))

canvas.create_text(
    -967.0, -372.5,
    text = "USER ACCOUNT ",
    fill = "#000000",
    font = ("Inter-Bold", int(55.0)))

window.resizable(False, False)
window.mainloop()

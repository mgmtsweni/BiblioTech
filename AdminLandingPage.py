from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1524x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1524,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    -976.0, -361.0,
    text = "ADMIN ACCOUNT ",
    fill = "#000000",
    font = ("Inter-Bold", int(55.0)))

window.resizable(False, False)
window.mainloop()

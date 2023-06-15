from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 190, y = 631,
    width = 352,
    height = 86)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 190, y = 468,
    width = 352,
    height = 86)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    754.5, 518.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()

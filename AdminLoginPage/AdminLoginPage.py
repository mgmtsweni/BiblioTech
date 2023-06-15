from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#bb86fc")
canvas = Canvas(
    window,
    bg = "#bb86fc",
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
    x = 182, y = 674,
    width = 352,
    height = 86)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    364.0, 414.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 143.0, y = 382,
    width = 442.0,
    height = 63)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    364.0, 560.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 143.0, y = 528,
    width = 442.0,
    height = 63)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    754.5, 512.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()

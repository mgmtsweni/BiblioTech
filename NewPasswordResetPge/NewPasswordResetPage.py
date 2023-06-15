from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#f46524")
canvas = Canvas(
    window,
    bg = "#f46524",
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
    x = 102, y = 677,
    width = 422,
    height = 84)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    312.5, 405.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 80.0, y = 366,
    width = 465.0,
    height = 77)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    312.5, 575.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 80.0, y = 536,
    width = 465.0,
    height = 77)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    753.5, 512.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()

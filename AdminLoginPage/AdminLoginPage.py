from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1524x1024")
window.configure(bg = "#bb86fc")
canvas = Canvas(
    window,
    bg = "#bb86fc",
    height = 1024,
    width = 1524,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file="img_textBox0.png")
entry0_bg = canvas.create_image(
    -989.0, -193.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = -1210.0, y = -226,
    width = 442.0,
    height = 63)

canvas.create_text(
    -1148.0, -96.0,
    text = "Password",
    fill = "#ffffff",
    font = ("None", int(25.0)))

entry1_img = PhotoImage(file="img_textBox1.png")
entry1_bg = canvas.create_image(
    -989.0, -47.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = -1210.0, y = -80,
    width = 442.0,
    height = 63)

canvas.create_text(
    -1148.0, -249.0,
    text = "Username",
    fill = "#ffffff",
    font = ("None", int(25.0)))

canvas.create_text(
    -1003.0, -358.0,
    text = "ADMIN  ",
    fill = "#000000",
    font = ("Inter-Bold", int(55.0)))

window.resizable(False, False)
window.mainloop()

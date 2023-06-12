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

canvas.create_text(
    -1081.0, -321.0,
    text = "Don’t have an account yet? ",
    fill = "#ffffff",
    font = ("Inter-Bold", int(23.0)))

canvas.create_text(
    -811.0, -321.0,
    text = "Sign Up",
    fill = "#ffffff",
    font = ("Inter-Bold", int(23.0)))

canvas.create_text(
    -1120.5, 37.0,
    text = "Keep me loged in",
    fill = "#ffffff",
    font = ("None", int(21.0)))

canvas.create_text(
    -864.0, 38.0,
    text = "Forgot Password?",
    fill = "#ffffff",
    font = ("None", int(21.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    -1003.5, -173.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = -1221.0, y = -206,
    width = 435.0,
    height = 63)

canvas.create_text(
    -1171.0, -70.0,
    text = "Password",
    fill = "#ffffff",
    font = ("None", int(25.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    -1003.5, -27.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = -1221.0, y = -60,
    width = 435.0,
    height = 63)

canvas.create_text(
    -1166.0, -217.0,
    text = "Username",
    fill = "#ffffff",
    font = ("None", int(25.0)))

canvas.create_text(
    -1003.0, -376.0,
    text = "Welcome Back!",
    fill = "#ffffff",
    font = ("Inter-Bold", int(45.0)))

window.resizable(False, False)
window.mainloop()

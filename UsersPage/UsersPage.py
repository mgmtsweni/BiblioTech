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

canvas.create_text(
    330.0, 75.0,
    text = "Available",
    fill = "#000000",
    font = ("Inter-Bold", int(30.0)))

canvas.create_text(
    629.5, 75.0,
    text = "Search",
    fill = "#000000",
    font = ("Inter-Bold", int(30.0)))

canvas.create_text(
    905.5, 79.0,
    text = "Order",
    fill = "#000000",
    font = ("Inter-Bold", int(30.0)))

canvas.create_text(
    1144.0, 79.0,
    text = "More",
    fill = "#000000",
    font = ("Inter-Bold", int(30.0)))

canvas.create_text(
    1143.5, 228.0,
    text = "Services",
    fill = "#000000",
    font = ("Inter-Bold", int(30.0)))

canvas.create_text(
    1143.5, 162.0,
    text = "About",
    fill = "#000000",
    font = ("Inter-Bold", int(30.0)))

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    710.0, 425.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()

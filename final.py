import tkinter as tk
from PIL import Image, ImageTk
import turtle
import markovify
import random
import math
import sys

def draw_heart(t, on_complete=None):
    t.speed(0)
    t.pensize(0.5)
    t.hideturtle()
    t.penup()
    t.color("LightCoral")
    for i in range(800):
        x = 15 * math.sin(i) ** 3 * 20
        y = (12 * math.cos(i) - 5 * math.cos(2 * i) - 2 * math.cos(3 * i) - math.cos(4 * i)) * 20
        t.goto(0,0)
        t.goto(x, y)
        t.pendown()
        
    
    if on_complete:
        on_complete()

def generate_birthday_wish_markov(text, sonakshi, keywords):
    text_mod = markovify.Text(text)
    if keywords:
        gen = text_mod.make_sentence()
        random_word = random.choice(["amazing", "fantastic", "joyful", "lovely", "sparkling"])
        if not gen:
            return f"Happy birthday, {sonakshi}!  Wishing you a {random_word} day{text}."
        else:
            return f"Happy birthday, {sonakshi}! {gen} {random_word} Wishing you a wonderful day."

def main_gui():
    window = tk.Tk()
    window.title("Birthday Wish")
    window.geometry("600x600")

    # Tkinter canvas for images and text overlays
    canvas = tk.Canvas(window, width=600, height=600, highlightthickness=0, bg="MistyRose")
    canvas.pack(fill="both", expand=True)

    # Embed turtle canvas for heart
    turtle_canvas = turtle.ScrolledCanvas(window, width=600, height=600)
    turtle_canvas.place(x=0, y=0)
    screen = turtle.TurtleScreen(turtle_canvas)
    screen.bgcolor("MistyRose")
    t = turtle.RawTurtle(screen)

    # Prepare images
    img1 = ImageTk.PhotoImage(Image.open("pic.gif").resize((600, 600)))
    img2 = ImageTk.PhotoImage(Image.open("balloons-sparkle.gif").resize((600, 600)))
    img3 = ImageTk.PhotoImage(Image.open("download (1).gif").resize((600, 600)))
    canvas.img1 = img1
    canvas.img2 = img2
    canvas.img3 = img3

    # Load text data and generate wish
    data_file = "hey.txt"
    keywords = ["happy", "birthday", "wish", "wonderful", "day", "cute", "hugs"]
    try:
        with open(data_file, 'r', encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        text = "Happy Birthday!"
    ai_message = generate_birthday_wish_markov(text, "sonakshi", keywords)

    def show_pic_gif():
        turtle_canvas.place_forget()  # Hide turtle canvas
        canvas.delete("all")
        canvas.create_image(700, 300, anchor=tk.CENTER, image=canvas.img1)
        window.after(1000, show_balloons_gif)

    def show_balloons_gif():
        canvas.delete("all")
        canvas.create_image(700, 300, anchor=tk.CENTER, image=canvas.img2)
        window.after(1000, show_final_gif_and_text)

    def show_final_gif_and_text():
        canvas.delete("all")
        canvas.create_image(700, 300, anchor=tk.CENTER, image=canvas.img3)
        canvas.create_text(700, 520, text=ai_message, font=("Arial", 20), fill="Maroon", width=500, anchor=tk.CENTER, justify="center")

    # Sequence: draw heart, then show images/text
    def after_heart():
        show_pic_gif()

    draw_heart(t, on_complete=after_heart)

    window.mainloop()

if __name__ == "__main__":
    main_gui()

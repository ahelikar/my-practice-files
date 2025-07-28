import tkinter as tk
import turtle
import math
import markovify
import random
import time
import threading
from PIL import Image, ImageTk
# import thread  # Removed because 'thread' does not exist in Python 3 and is not used in this script
import turtle
import math
# turtle.Screen(canvas).bgcolor("cyan")  # Removed because 'canvas' is not defined and turtle.Screen() does not take arguments
# Removed the global _show_backgrnd_and_message function because 'canvas' is not defined in this scope.
# The correct implementation is already inside the main_gui() function where 'canvas' is defined.

def draw_heartfull(canvas):
    pass
# canvas   # Placeholder for canvas, to be defined in main_gui()
# Removed the global _show_backgrnd_and_message function because 'canvas' is not defined in this scope.

def draw(k):
    return 15*math.sin(k)**3
def draw_heart( x):
    return 12* math.cos(x)-5*\
math.cos(2*x)-2*\
math.cos(3*x)-\
math.cos(4*x)
t=turtle.Turtle()
turtle.Screen().bgcolor("cyan")
# Set the background color for the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("cyan")
t.speed(0)
t.pensize(0.5)

t.hideturtle()
t.penup()

for i in range(500):
    y=t.goto(draw(i) * 20,draw_heart(i) * 20)
    for i in range(1):
        t.color("MediumVioletRed")
    for i in range(4):
        t.color("PaleVioletRed")
    
    t.pendown()
    t.penup()
    
    t.pendown()
    def generate_ai_message():
        try:
            with open("hey.txt", 'r', encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print("Error:The file was not found")
            exit()
def generate_birthday_wish_markov(text, sonakshi, keywords):
    #if not text:
    # return f"Happy birthday,{sonakshi}! Wishing You a wonderful day1"
    text_mod = markovify.Text(text)
    if keywords:
        gen = text_mod.make_sentence()
        # Add a random word to the generated sentence
        random_word = random.choice(["amazing", "fantastic", "joyful", "lovely", "sparkling"])
        if not gen:
            return f"Happy birthday, {sonakshi}!  Wishing you a {random_word} day{text}."
        else:
            return f"Happy birthday, {sonakshi}! {gen} {random_word} Wishing you a wonderful day."
data_file="hey.txt"
keywords=["happy","birthday","wish","wonderful","day","cute","hugs"]
try:
    with open(data_file, 'r', encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("Error:The file was not found")
    exit()
print(generate_birthday_wish_markov(text, "sonakshi", keywords))
# Example implementation: show the message label
bg_image=Image.open("download (1).gif")
bg_photo=ImageTk.PhotoImage(bg_image)
    
    
t.hideturtle()
t.color("plum")
#turtle.write(generate_birthday_wish_markov(text, "sonakshi", keywords), align="center", font=("Waltograph", 16, "normal"))
# The following lines use 'canvas', which is not defined in this scope.
# Move them inside the main_gui() function where 'canvas' is defined.
# canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)
# canvas.bgphoto=bg_photo  # Keep a reference to avoid garbage collection

Screen=turtle.Screen()
x=Screen.bgpic("download (1).gif")
p=Screen.bgpic("pic.gif")
u=Screen.bgpic("balloons-sparkle.gif")
Screen.ontimer(y,5)
t.clear()
Screen.ontimer(p,5)
'''time.sleep(2)
Screen.ontimer(u,5)
time.sleep(2)
Screen.ontimer(x,5)'''
Screen.mainloop()


def main_gui():
    window = tk.Tk()
    window.title("Birthday Wish")
    canvas = tk.Canvas(window, width=500, height=500)
    canvas.pack()
    message_label = tk.Label(window, text="Happy Birthday Sonakshi!", font=("Arial", 24))
    message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def _show_backgrnd_and_message():
        # Only use ImageTk if available and image file exists
        try:
            bg_image = Image.open("download (1).jpg")
            bg_photo = ImageTk.PhotoImage(bg_image)
            canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)
            canvas.bgphoto = bg_photo  # Keep a reference to avoid garbage collection
        except Exception as e:
            print("Background image could not be loaded:", e)
        ai_message = generate_birthday_wish_markov(text, "sonakshi", keywords)
        canvas.config(bg="lavender")
        message_label.config(bg="pink", fg="plum")
        message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        message_label.config(text=ai_message)
        message_label.lift()

    def start_sequence():
        _show_backgrnd_and_message()

    start_sequence()
    window.mainloop()
if __name__ == "__main__":
    main_gui()
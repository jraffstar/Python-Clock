import tkinter as tk
import pygame
import datetime
import turtle
from tkinter import messagebox
global colour
global clockSize
pygame.mixer.init()

clockSize = 200
# --- Setup ---
t = turtle.Turtle()
c = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#000000")
screen.title("TRUE CLOCK")

root = screen._root  # Get the Tkinter root
menubar = tk.Menu(root)

# --- Colours ---#
colourSet1 = ["#BF092F","#132440","#16476A","#3B9797"]
colourSet2 = ["#FDEB9E","#000B58","#003161","#006A67"]
colourSet3 = ["#F78D60","#0D1164","#640D5F","#EA2264"]
colourSet4 = ["#EFE4D2","#131D4F","#254D70","#954C2E"]
colourSet5 = ["#FFFD8C","#793FDF","#7091F5","#97FFF4"]
colourSet6 = ["#777C6D","#B7B89F","#CBCBCB","#EEEEEE"]
colour = colourSet1

# --- Options menu ---
options_menu = tk.Menu(menubar, tearoff=0)

timezone_menu = tk.Menu(menubar, tearoff=0)
timezone_menu.add_command(label="England", command=lambda: print("1"))
timezone_menu.add_command(label="England", command=lambda: print("2"))
timezone_menu.add_command(label="England", command=lambda: print("3"))
options_menu.add_cascade(label="Timezones", menu=timezone_menu)

# changes the size of the clock
def clockUp(z):
    global clockSize
    clockSize += z
    clock()
def clockDown(z):
    global clockSize
    clockSize -= z
    clock()

clock_size_menu = tk.Menu(menubar, tearoff=0)
clock_size_menu.add_command(label="ClockSize +50", command=lambda: clockUp(50))
clock_size_menu.add_command(label="ClockSize  -50", command=lambda: clockDown(50))
clock_size_menu.add_separator()
clock_size_menu.add_command(label="ClockSize +10", command=lambda: clockUp(10))
clock_size_menu.add_command(label="ClockSize  -10", command=lambda: clockDown(10))
options_menu.add_cascade(label="Clock Size", menu=clock_size_menu)

options_menu.add_separator()
# --- Help menu ---
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Bro Its A Watch"))
options_menu.add_cascade(label="Help", menu=help_menu)

options_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Options", menu=options_menu)

turtle.tracer(0)  # Disable auto-updates for smooth animation

def clock():
    global colour
    global clockSize
    c.penup()
    c.setheading(0)
    c.clear()
    # Draw static parts of the clock (circles)
    c.goto(0, 0)
    c.pendown()
    c.pencolor(colour[0])
    c.dot(clockSize)
    c.penup()
    c.goto(0, -clockSize)
    c.pendown()
    c.pensize(2)
    c.circle(clockSize)
    c.penup()
    c.goto(0, -(clockSize - (clockSize/10)))
    c.pendown()
    c.pensize(5)
    c.circle(clockSize - (clockSize/10))
    c.hideturtle()
    for x in range(12):
        c.penup()
        c.pensize(5)
        c.setheading(90)
        c.goto(0, 0)
        c.right(6 * 5 * x)
        c.forward(clockSize - (clockSize/10))
        c.pendown()
        c.forward((clockSize/40))
# --- Colour Menu ---
def colourset(cum):
    global colour
    colour = cum
    clock()


circle = tk.PhotoImage(file="assets/Circle.png")
desert = tk.PhotoImage(file="assets/Desert.png")
stone = tk.PhotoImage(file="assets/Stone.png")
sun = tk.PhotoImage(file="assets/Sun.png")
snow = tk.PhotoImage(file="assets/Snow.png")

colour_menu = tk.Menu(menubar, tearoff=0)
colour_menu.add_command(label="Colour Set 1 (Original)",image=circle,compound="left", command=lambda: colourset(colourSet1))
colour_menu.add_separator()
colour_menu.add_command(label="Colour Set 2 (Desert)"  ,image=desert,compound="left", command=lambda: colourset(colourSet2))
colour_menu.add_command(label="Colour Set 3 (Peach)"   ,image=desert,compound="left", command=lambda: colourset(colourSet3))
colour_menu.add_command(label="Colour Set 4 (Snow)"    ,image=snow  ,compound="left", command=lambda: colourset(colourSet4))
colour_menu.add_command(label="Colour Set 5 (Sun)"     ,image=sun   ,compound="left", command=lambda: colourset(colourSet5))
colour_menu.add_command(label="Colour Set 6 (Stone)"   ,image=stone ,compound="left", command=lambda: colourset(colourSet6))
menubar.add_cascade(label="Colour", menu=colour_menu)

# --- Attach the menu to the window ---
root.config(menu=menubar)
# --- Clock setup ---
def hand(y, size, pensize, ofset, color):
    global clockSize
    t.penup()
    t.pencolor(color)
    t.pensize(pensize)
    t.setheading(90)
    t.goto(0, 0)
    t.pendown()
    x = y
    t.right(6 * ofset * x)
    t.forward(clockSize / size)
# --- Update clock hands repeatedly using root.after() ---
def update_clock():
    global colour
    t.clear()
    now = datetime.datetime.now()
    hand(now.hour % 12,  3, 10, 5, colour[1])
    hand(now.minute   ,  2, 5 , 1, colour[2])
    hand(now.second   ,  1, 2 , 1, colour[3])
    t.goto(0, 0)
    t.pencolor("#ffffff")
    t.dot(10)
    turtle.update()
    # Schedule next update in 1000 ms (1 second)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/tick.mp3'))
    root.after(1000, update_clock)
# Start the clock loop
c.clear()
t.clear()
clock()
update_clock()
turtle.done()

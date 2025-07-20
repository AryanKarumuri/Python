#Using RGB

import turtle as t
import random

Tom = t.Turtle()
t.colormode(255)

def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = (r, g, b)
    return color_code

directions = [0, 90, 180, 270]
Tom.pensize(20)
Tom.speed("fastest")



for _ in range(400):
    Tom.color(rgb_color())
    Tom.forward(30)
    Tom.setheading(random.choice(directions))

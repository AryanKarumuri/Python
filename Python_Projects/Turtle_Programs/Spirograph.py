import turtle as t
import random

Tom = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        Tom.speed("fastest")
        Tom.color(random_color())
        Tom.circle(100)
        Tom.setheading(Tom.heading() + size_of_gap)

draw_spirograph(5)
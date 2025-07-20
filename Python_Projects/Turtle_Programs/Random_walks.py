import turtle as t
import random

Tom = t.Turtle()


colors = ["dim gray", "light slate gray", "indian red", "salmon", "gold", "green yellow", "LightSeaGreen", "wheat", "indigo", "dark slate blue"]
directions = [0, 90, 180, 270]
Tom.pensize(20)
Tom.speed("fast")



for _ in range(400):
    Tom.color(random.choice(colors))
    Tom.forward(30)
    Tom.setheading(random.choice(directions))

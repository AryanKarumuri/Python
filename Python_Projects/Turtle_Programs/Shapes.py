import turtle as t
import random

Tom = t.Turtle()
colors = ["chartreuse", "firebrick", "tomato", "purple", "gold", "mediumblue"]

def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        Tom.forward(80)
        Tom.right(angle)

for i in range(3, 11):
    Tom.color(random.choice(colors))
    draw_shape(i)
        

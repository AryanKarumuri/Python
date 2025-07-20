"""
import colorgram
colors = colorgram.extract("image.png", 20)
rgb_colors = []
for i in colors:
    #Method-1
    #r = i.rgb.r
    #g = i.rgb.g
    #b = i.rgb.b
    #new_color = (r, g, b)
    
    #Method-2
    new_color = (i.rgb.r, i.rgb.g, i.rgb.b)
    rgb_colors.append(new_color)
print(rgb_colors)
"""
import turtle as t
import random

rgb_colors = [(28, 39, 50), (0, 174, 238), (12, 112, 186), (220, 234, 241), (113, 176, 211), (180, 159, 151), (182, 23, 47), (225, 66, 52), (58, 32, 127), (33, 31, 31), (103, 91, 88), (191, 142, 149), (151, 63, 76), (13, 59, 13), (204, 75, 83), (148, 164, 159), (67, 21, 26)]
t.colormode(255)
Tom = t.Turtle()
Tom.speed("fastest")
Tom.penup()
Tom.hideturtle()
Tom.setheading(225)
Tom.forward(300)
Tom.setheading(0)

def turn_right():
    Tom.setheading(90)
    Tom.forward(50)
    Tom.setheading(0)
    
def turn_left():
    Tom.setheading(90)
    Tom.forward(50)
    Tom.setheading(180)
    
for _ in range(5):
    for _ in range(10):
        Tom.dot(20, random.choice(rgb_colors))
        Tom.forward(50)
    turn_left()
    for _ in range(10):
        Tom.forward(50)
        Tom.dot(20, random.choice(rgb_colors))
    turn_right()
        
screen = t.Screen()
screen.exitonclick()





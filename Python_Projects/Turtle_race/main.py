from turtle import Turtle, Screen
import random

on_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter one color(red, orange, yellow, green, blue, purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_coordinates[i])
    all_turtles.append(new_turtle)

if user_guess:
    on_race = True
    
while on_race:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            on_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
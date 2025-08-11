from turtle import Turtle, Screen
import random

def number_of_sides(sides):
    tim.color(random.choice(colors))
    angle = 360 / sides
    for _ in range(sides):
        tim.right(angle)
        tim.forward(100)

def forward_dot_line():
    for i in range(0, 30):
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()

colors = ["cyan", "slate gray", "firebrick", "forest green", "goldenrod"]
tim = Turtle()

number = 3
while number <= 9:
    number_of_sides(number)
    number += 1

screen = Screen()
screen.exitonclick()
import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
t=Turtle()

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

directions=[0,90,270,180]
t.width(10)
t.speed("fast")

for i in range(300):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))

screen=Screen()
screen.exitonclick()

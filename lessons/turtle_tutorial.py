"""Turtle tutorial."""
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.color(99, 204, 250)


leo.goto(45, 60)

leo.begin_fill()


i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()

done()
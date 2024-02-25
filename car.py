from turtle import Turtle
import random

colors = ["red", "blue", "yellow", "green", "black", "orange", "violet", "pink"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1.8, 1)
        self.color(random.choice(colors))
        self.penup()
        self.setheading(90)
        self.goto(380, random.randint(-340, 340))

    def move(self):
        new_x = self.xcor() - 10
        new_y = self.ycor()
        self.goto(new_x, new_y)

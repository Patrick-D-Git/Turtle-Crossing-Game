from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.starting_position()

    def move_up(self):

        self.forward(10)

    def starting_position(self):
        self.goto(0, -380)



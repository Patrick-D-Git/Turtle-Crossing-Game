from turtle import Turtle


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.starting_line()
        self.penup()
        self.hideturtle()
        self.goto(-335, 360)
        self.level = 1
        self.game_speed = 0.1
        self.refresh()

    def refresh(self):
        self.clear()
        self.starting_line()
        self.finish_line()
        self.goto(-335, 370)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 15, "normal"))

    def increase_level(self):
        self.level += 1
        self.game_speed *= 0.5
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 30, "normal"))

    def starting_line(self):
        self.pencolor("black")
        self.pensize(2)
        self.goto(400, -360)
        self.pendown()
        self.goto(-400, -360)
        self.penup()
        self.goto(320, -385)
        self.write("Starting Line", align="center", font=("Courier", 15, "normal"))

    def finish_line(self):
        self.pencolor("black")
        self.pensize(2)
        self.goto(400, 360)
        self.pendown()
        self.goto(-400, 360)
        self.penup()
        self.goto(320, 370)
        self.write("Finish Line", align="center", font=("Courier", 15, "normal"))
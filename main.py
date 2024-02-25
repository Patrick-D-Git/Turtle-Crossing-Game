from turtle import Screen
from player import Player
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        player.increase_speed()
        player.starting_position()

screen.exitonclick()

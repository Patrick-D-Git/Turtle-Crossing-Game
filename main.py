from turtle import Screen
from player import Player
from car import Car
from board import Board
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
board = Board()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True

cars = []
cycle_count = 0
while game_is_on:
    time.sleep(board.game_speed)
    screen.update()

    cycle_count += 1
    if cycle_count == 4:
        new_car = Car()
        cars.append(new_car)
        cycle_count = 0

    for car in cars:
        car.move()

        if player.distance(car) < 20:
            game_is_on = False
            board.game_over()

    if player.ycor() > 380:
        player.starting_position()
        board.increase_level()


screen.exitonclick()

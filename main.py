from turtle import Screen
from player import Player
from car import Car
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True

cars = []
cycle_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cycle_count += 1
    if cycle_count == 4:
        new_car = Car()
        cars.append(new_car)
        cycle_count = 0

    for car in cars:
        car.move()

    if player.ycor() > 380:
        player.increase_speed()
        player.starting_position()

screen.exitonclick()

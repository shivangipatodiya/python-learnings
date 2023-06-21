import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_load = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_load.create_new_car()
    car_load.move_cars()

    for car in car_load.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

        if player.cross_finish_line():
            scoreboard.level_up()
            car_load.increase_speed()
            player.go_to_starting_point()


screen.exitonclick()

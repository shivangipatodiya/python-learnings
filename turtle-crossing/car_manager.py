from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        random_chance = random.randint(1, 20)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.speed("slow")
            car.turtlesize(1, 2)
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

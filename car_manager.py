import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.total_cars = []
        self.no_of_increment = 0
    def create(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.goto(300,random.randint(-250,250))
            new_car.setheading(180)
            self.total_cars.append(new_car)

    def move(self):
        for cars in self.total_cars:
            cars.forward(STARTING_MOVE_DISTANCE + (self.no_of_increment*MOVE_INCREMENT))

    def increment(self):
        self.no_of_increment += 1
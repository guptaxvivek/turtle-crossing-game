import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
screen.onkey(player.move,"Up")
car = CarManager()

car.create()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()
    #collision with car
    for carc in car.total_cars:
        if player.distance(carc) < 40:
            game_is_on = False
            score.end()
    #level pass
    if player.ycor() >= 280:
        player.success()
        score.update()
        car.increment()

screen.exitonclick()
from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
score = Scoreboard()
carManager = CarManager()

screen.listen()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_cars()
    carManager.move()
    screen.onkey(player.move, "Up")
    if player.ycor() > 300:
        player = Player()
        score.next_level()
        carManager.level_up()

    for car in carManager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False
screen.exitonclick()

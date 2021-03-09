from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars =[]
        self.speed = STARTING_MOVE_DISTANCE



    def create_cars(self):
        i = random.randint(1,7)
        if i==1:
         new_car = Turtle()
         new_car.shape("square")
         new_car.turtlesize(stretch_wid=1, stretch_len=2)
         new_car.penup()
         new_car.setheading(180)
         new_car.color(random.choice(COLORS))
         new_car.goto(310, random.randint(-250, 250))
         self.all_cars.append(new_car)



    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)


    def level_up(self):
        self.speed += MOVE_INCREMENT
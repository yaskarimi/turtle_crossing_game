FONT = ("Courier", 24, "normal")
LEVEL = 1
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = LEVEL
        self.setposition(-270, 260)
        self.write(f"level:{self.level}", False, font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"level:{self.level}", False, font=FONT)

    def game_over(self):
        self.clear()
        self.write("Game over", False, font=FONT)
        self.penup()
        self.goto(0, 0)

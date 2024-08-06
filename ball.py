from turtle import Turtle
from random import randint


class Ball(Turtle):
    random_number = randint(0, 360)
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        """Reverse the x/y coordinates"""
        self.x_move *= -1
        self.y_move *= -1

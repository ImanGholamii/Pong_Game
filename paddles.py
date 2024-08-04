from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def right_paddle(self):
        self.goto(x=550, y=0)

    def left_paddle(self):
        self.goto(x=-550, y=0)

    def up(self):
        self.speed("fastest")
        self.setheading(90)
        self.fd(20)
        self.setheading(0)


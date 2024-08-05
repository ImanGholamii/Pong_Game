from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.speed("fast")
        self.penup()
        self.start()
        self.move()

    def start(self):
        if self.position() == (0, 0):
            self.setheading(randint(0, 180))
            self.fd(40)
            while self.position() != (0, 0):
                self.fd(40)

    def move(self):
        """detect boards and Collision up and down corners"""

        if self.xcor() < 590 and self.xcor() > -590 and self.ycor() < 390 and self.ycor() > -390:
            if self.heading() < 90 or self.heading() > 0:
                self.setheading(randint(-89, 1))
                self.fd(40)
            elif self.heading() < 0 or self.heading() > -90:
                self.setheading(randint(0, 89))
                self.fd(40)
            elif self.heading() < 180 or self.heading() > 90:
                self.setheading(randint(89, 179))
                self.fd(40)
            elif self.heading() < 270 or self.heading() > 180:
                self.setheading(randint(89, 179))
            else:
                self.fd(40)
        elif self.ycor() >= 390 or self.ycor() <= -390:
            pass



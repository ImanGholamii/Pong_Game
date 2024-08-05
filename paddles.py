from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 220:
            self.goto(x=self.xcor(), y=self.ycor() + 50)

    def down(self):
        if self.ycor() > -300:
            self.goto(x=self.xcor(), y=self.ycor() - 50)

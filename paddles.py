from turtle import Turtle

class Paddle(Turtle):
    def __init_(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=20, stretch_len=100)
        self.color("white")
        self.right_paddle()
        self.left_paddle()

    def right_paddle(self):
        self.penup()
        self.setpos(x=-550, y=0)

    def left_paddle(self):
        self.setpos(x=550, y=0)


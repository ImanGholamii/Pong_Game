from turtle import Turtle

class board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.draw_vertical_line()
        self.draw_horizontal_line(x=-600, y=300)
        self.draw_horizontal_line(x=-600, y=-300)


    def draw_vertical_line(self):
        self.teleport(x=0, y=300)
        self.setheading(-90)
        while self.ycor() > -400:
            self.pensize(width=3)
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)

    def draw_horizontal_line(self, x, y):
        self.teleport(x, y)
        while self.xcor() < -x:
            self.setheading(0)
            self.pensize(width=3)
            self.pendown()
            self.fd(20)

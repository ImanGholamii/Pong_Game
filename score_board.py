from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.color("white")
        self.hideturtle()

    def add_point(self):
        self.point += 1

    def show_point(self):
        self.penup()
        self.setpos(x=-30, y=300)
        self.write(arg=f"{self.point}", align=ALIGNMENT, font=FONT)
        self.setpos(x=30, y=300)
        self.write(arg=f"{self.point}", align=ALIGNMENT, font=FONT)


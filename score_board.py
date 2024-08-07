from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.position = position
        self.point = 0
        self.color("white")
        self.hideturtle()

    def add_point(self):
        self.point += 1

    def show_point(self):
        self.penup()
        self.setpos(self.position)
        self.write(arg=f"{self.point}", align=ALIGNMENT, font=FONT)

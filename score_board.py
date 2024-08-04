from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x=0, y=300)
        self.write(arg=f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
        self.draw_line()

    def draw_line(self):
        self.setheading(-90)
        while self.ycor() > -400:
            self.pensize(width=3)
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)


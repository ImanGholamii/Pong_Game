from turtle import Turtle, Screen
from score_board import ScoreBoard
# objects
screen = Screen()
score_board = ScoreBoard()

# Screen Setups
screen.setup(width=1200, height=660)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0, 0)

screen.exitonclick()

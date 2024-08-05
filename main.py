from turtle import Turtle, Screen
from score_board import ScoreBoard
from paddles import Paddle
from ball import Ball

# Screen Setups
screen = Screen()
screen.setup(width=1200, height=660)
screen.bgcolor('navy')
screen.title("Pong Game")
screen.tracer(0, 0)

# objects
score_board = ScoreBoard()

screen.tracer(1, 10)

right_paddle = Paddle()
right_paddle.right_paddle()
left_paddle = Paddle()
left_paddle.left_paddle()

ball = Ball()
# key events

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')


screen.update()
screen.exitonclick()

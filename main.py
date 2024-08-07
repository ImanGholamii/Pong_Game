from turtle import Screen
from score_board import ScoreBoard
from paddles import Paddle
from ball import Ball
from time import sleep
from table import Board

# Screen Setups
screen = Screen()
screen.setup(width=1200, height=660)
screen.bgcolor('navy')
screen.title("Pong Game")
screen.tracer(0, 0)

# objects
right_score_board = ScoreBoard((30, 300))
left_score_board = ScoreBoard((-30, 300))
bord = Board()
# screen.tracer(1, 10)

right_paddle = Paddle((550, 0))
left_paddle = Paddle((-550, 0))

ball = Ball()
# key events

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_is_on = True
while game_is_on:
    sleep(0.03)
    right_score_board.show_point()
    left_score_board.show_point()
    screen.update()
    ball.move()
    # Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Paddle and add points
    if ball.xcor() > 530 and ball.distance(right_paddle) < 50 or ball.xcor() < -530 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
    elif ball.xcor() > 550:
        ball.bounce_x()
        right_score_board.clear()
        right_score_board.add_point()
    elif ball.xcor() < -550:
        ball.bounce_x()
        left_score_board.clear()
        left_score_board.add_point()

screen.exitonclick()

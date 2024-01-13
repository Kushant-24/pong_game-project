from turtle import Screen
from paddles import Paddles
from pong import Pong
import time
screen = Screen()
screen.setup(width=1100, height=600)
screen.bgcolor("black") 
screen.title("PONG GAME by k.s.negi")
screen.tracer(0)
screen.listen()

# -------------------Game Variable---------------------- #

board = Paddles() # Two paddles
left_board = board.left_pad # left paddle
right_board = board.right_pad # right paddle
ball = Pong() # Pong ball
is_on = True # Game on/off 

# -------------------Game Controls---------------------- #
screen.onkey(board.l_upkey, "w")
screen.onkey(board.l_downkey, "s")
screen.onkey(board.r_upkey, "Up")
screen.onkey(board.r_downkey, "Down")


# -------------------Game Loop---------------------- #
while is_on:
    time.sleep(0.05)
    screen.update()
    ball_angle = ball.heading()
    ball.forward(10)
    if ball.ycor() >=290 or ball.ycor() <= -290:
        ball.setheading(360-ball_angle)
    if ball.distance(left_board) < 20 or ball.distance(right_board) < 20:
        ball.setheading(180-ball_angle)
screen.exitonclick()
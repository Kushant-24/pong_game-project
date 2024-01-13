from turtle import Screen
import paddles
import pong
import time
screen = Screen()
screen.setup(width=1100, height=600)
screen.bgcolor("black") 
screen.title("PONG GAME by k.s.negi")
screen.tracer(0)
screen.listen()

# -------------------Game Variable---------------------- #

board = paddles.Paddles() # left/right paddles
ball = pong.Pong() # Pong ball
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
    ball.ball_motion()
screen.exitonclick()
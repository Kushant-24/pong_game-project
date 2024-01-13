from turtle import Turtle
import random
directions = [45,160,210,330]
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setheading(random.choice(directions))
        # self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.speed(2)
    def ball_motion(self):
        self.forward(10)

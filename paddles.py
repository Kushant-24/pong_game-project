from turtle import Turtle
class Paddles:
    def __init__(self):
        self.x_coordinate = [-530,530]
        self.pads = []
        self.single_pad()
        self.left_pad = self.pads[0] 
        self.right_pad = self.pads[1] 
    def single_pad(self):
        for i in range(2):
            self.pad = Turtle('square')
            self.pad.penup()
            self.pad.shapesize(1,4)
            self.pad.setheading(90)
            self.pad.color('white')
            self.pad.goto(self.x_coordinate[i],0)
            self.pads.append(self.pad)
    def l_upkey(self):
        if self.left_pad.ycor() < 260:
            self.left_pad.forward(50)
    def l_downkey(self):
        if self.left_pad.ycor() > -260:
            self.left_pad.forward(-50)
    def r_upkey(self):
        if self.right_pad.ycor() < 260:
            self.right_pad.forward(50)
    def r_downkey(self):
        if self.right_pad.ycor() > -260:
            self.right_pad.forward(-50)
import turtle
class Paddles:
    def __init__(self):
        self.x_coordinate = [-530,530]
        self.pads = []
        self.single_pad()
        self.left_pad = self.pads[0] 
        self.right_pad = self.pads[1] 
    def single_pad(self):
        for i in range(2):
            self.pad = turtle.Turtle('square')
            self.pad.penup()
            self.pad.shapesize(1,4)
            self.pad.setheading(90)
            self.pad.color('white')
            self.pad.goto(self.x_coordinate[i],0)
            self.pads.append(self.pad)
    def l_upkey(self):
        self.left_pad.forward(100)
    def l_downkey(self):
        self.left_pad.forward(-100)
    def r_upkey(self):
        self.right_pad.forward(100)
    def r_downkey(self):
        self.right_pad.forward(-100)


screen = turtle.Screen()
screen.setup(width=1100, height=600)
screen.bgcolor("black") 
screen.title("PONG GAME by k.s.negi")
screen.listen()
board = Paddles()
screen.onkey(board.l_upkey, "w")
screen.onkey(board.l_downkey, "s")
screen.onkey(board.r_upkey, "Up")
screen.onkey(board.r_downkey, "Down")


screen.exitonclick()
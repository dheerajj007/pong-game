from turtle import Turtle

class Paddle:

    def __init__(self, starting_positions):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.starting_positions = starting_positions
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(self.starting_positions)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        if self.paddle.ycor() < 238:
            self.paddle.goto(self.paddle.xcor(), new_y)
    
    def go_down(self):
        new_y = self.paddle.ycor() - 20
        if self.paddle.ycor() > -238:
            self.paddle.goto(self.paddle.xcor(), new_y)


from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()


GAME_IS_ON = True

while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()
        




screen.mainloop()

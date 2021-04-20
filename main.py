from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
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

scoreboard = ScoreBoard()

GAME_IS_ON = True

while GAME_IS_ON:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_screen()
        scoreboard.l_increase()
 
    if ball.xcor() < -380:
        ball.reset_screen()
        scoreboard.r_increase()


screen.mainloop()

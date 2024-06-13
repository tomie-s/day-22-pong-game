# PONG GAME
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# TODO 1: Create game screen with dividing line
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# TODO 2: Create the first paddle and have them move only on y-axis
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# TODO 3: Create the pong ball that bounces across screen.
ball = Ball()
# TODO 7: Keep track of the users score
score = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 4: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 5: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO 6: Handle ball once it misses the paddles
    if ball.xcor() > 400:
        ball.restart()
        score.point_for_l()

    if ball.xcor() < -400:
        ball.restart()
        score.point_for_r()


screen.exitonclick()

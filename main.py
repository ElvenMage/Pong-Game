# Pong Game Made by Elven Mage
from turtle import Turtle, Screen
from racket import Rackets
from ball import Ball
from scoreboard import Scoreboard
import time


def close_game():
    global game_is_on
    game_is_on = False


# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
# Objects
racket = Rackets()
ball = Ball()
scoreboard = Scoreboard()

# Listening for key presses
screen.listen()
screen.onkey(fun=racket.l_go_up, key="Up")
screen.onkey(fun=racket.l_go_down, key="Down")
screen.onkey(fun=racket.r_go_up, key="w")
screen.onkey(fun=racket.r_go_down, key="s")
screen.onkey(fun=close_game, key="c")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(racket.head2) < 50 and ball.xcor() > 320 or ball.distance(racket.head) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

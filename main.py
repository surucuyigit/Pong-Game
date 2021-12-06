import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score


def game():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    left_paddle = Paddle((-350, 0))
    right_paddle = Paddle((350, 0))
    ball = Ball()
    score = Score()

    screen.listen()
    screen.onkeypress(right_paddle.up, "Up")
    screen.onkeypress(right_paddle.down, "Down")
    screen.onkeypress(left_paddle.up,  "w")
    screen.onkeypress(left_paddle.down, "s")
    screen.onkey(reset, "r")
    screen.onkey(close, "Escape")

    game_continue = True
    while game_continue:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

    # To change the y direction after collision with top or bottom of the screen.
        if ball.ycor() < -280 or ball.ycor() > 280:
            ball.change_y()

    # # To solve the bouncing from back of paddle and edge problems
    #     if 330 <= ball.xcor() <= 340 and ball.distance(right_paddle) <= 60:
    #         ball.change_x()
    #
    #     if -340 <= ball.xcor() <= -330 and ball.distance(left_paddle) <= 60:
    #         ball.change_x()


    # To change the x direction after collision with paddles
        if ball.xcor() < -320 or ball.xcor() > 320:
            if ball.distance(right_paddle) < 54 or ball.distance(left_paddle) < 54:
                ball.change_x()


    # Determine the score
        if ball.xcor() < -350:
            ball.reset_position()
            score.right_point()

        if ball.xcor() > 350:
            ball.reset_position()
            score.left_point()

    screen.exitonclick()


def reset():
    Screen().clear()
    game()


def close():
    turtle.bye()


game()

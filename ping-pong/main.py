from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()

first_player = Paddle((350, 0))
second_player = Paddle((-350, 0))


screen.listen()
screen.onkey(first_player.go_up,"Up")
screen.onkey(first_player.go_down,"Down")

screen.onkey(second_player.go_up, "w")
screen.onkey(second_player.go_down, "s")


game_over = False

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(first_player) < 50 and ball.xcor() > 320 or ball.distance(second_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.second_player_scores()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.first_player_scores()





screen.exitonclick()
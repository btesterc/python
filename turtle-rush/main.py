import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.count_scores()
screen.onkey(player.move, "Up" )


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.random_cars()
    car_manager.move()

    for car in car_manager.car_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    if player.finish():
        player.start_position()
        car_manager.speed_up()
        scoreboard.inc_scores()








screen.exitonclick()

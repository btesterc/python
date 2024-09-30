import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
using_bet = screen.textinput(title="make your bed", prompt="enter a color")
colors = ["red", "orange", "blue", "yellow", "green", "purple"]
all_turtles = []
y = -70


for i in range(0,6):
    new_turtle = Turtle(shape="turtle", )
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y)
    y += 30
    all_turtles.append(new_turtle)


if using_bet:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == using_bet:
                print(f"You have won {winning_color} is the winning color. ")
            else:
                print(f"You have Lost  {winning_color} is the winning color. ")
        ran_dic = random.randint(0, 10)
        i.forward(ran_dic)










screen.exitonclick()
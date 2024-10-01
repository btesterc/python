from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.score = 1
        self.count_scores()


    def count_scores(self):
        self.write(f"level {self.score} ", align="center", font=FONT)

    def inc_scores(self):
        self.score += 1
        self.clear()
        self.write(f"level {self.score} ", align="center", font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)







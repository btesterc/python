from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./score.txt", mode="w") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.writing_score()
        self.hideturtle()


    def writing_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.writing_score()

    def inc_score(self):
        self.score += 1
        self.writing_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))


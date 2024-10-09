from turtle import  Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.keep_scores()



    def keep_scores(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    def first_player_scores(self):
        self.r_score += 1
        self.clear()
        self.keep_scores()

    def second_player_scores(self):
        self.l_score += 1
        self.clear()
        self.keep_scores()


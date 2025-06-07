from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.score}", align="center", font=("courier", 20, "normal"))
        self.hideturtle()

    def game_result(self):
        self.goto(0,0)
        self.write(f"Game Over.", align="center", font=("courier", 18, "normal"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("courier", 20, "normal"))
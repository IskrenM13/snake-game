from turtle import Turtle
with open("data.txt") as data:
    HIGH_SCORE = data.read()

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = int(HIGH_SCORE)
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 280)
        self.hideturtle()
        self.hideturtle()
        self.score_up()

    def score_up(self):
        self.undo()
        self.hideturtle()
        self.write(f"Your score: {self.score} High Score {self.high_score}", move=False, align='center', font=('Arial', 12, 'normal'))

    def highscore(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))

            self.high_score = self.score
        self.score = 0
        self.score_up()




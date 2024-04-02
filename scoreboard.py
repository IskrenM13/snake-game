from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
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
        self.write(f"Your score: {self.score}", move=False, align='center', font=('Arial', 12, 'normal'))

    def gameover(self):

        self.hideturtle()
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 30, 'normal'))

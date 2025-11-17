from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())

        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.write(f"Score-{self.score}     High Score-{self.highscore}", align="center", font=("Courier",15,"normal"))

    def inc_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score-{self.score}     High Score-{self.highscore}", align="center", font=("Courier",15,"normal"))

    '''def over(self):
        self.goto(0,0)
        self.write("GAME-OVER", align="center", font=("Courier",25,"normal"))
    '''

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score

            with open("data.txt",mode="w") as file:
                file.write(str(self.highscore))

        self.score=-1
        self.inc_score()


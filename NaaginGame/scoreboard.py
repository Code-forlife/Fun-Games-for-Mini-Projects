from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score : {self.score} Highest Score: {self.highscore}", move=False, align='center', font=('Courier', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  Highest Score: {self.highscore}", move=False, align='center', font=('Courier', 20, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def end_game(self):
    #     self.home()
    #     self.write("AA GAYE NAAGIN HATH ME", move= False, align="Center", font=('Courier ', 20, 'normal'))
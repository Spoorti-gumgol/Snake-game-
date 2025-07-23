from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score:
            high_score = score.read()
            high_score = int(high_score)
            self.high_score = high_score
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as score:
                high_score = str(self.high_score)
                score.write(high_score)
        self.score = 0
        self.update_scoreboard()

        


        
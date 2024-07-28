from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.scoreboard} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.scoreboard += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.scoreboard > self.high_score:
            self.high_score = self.scoreboard
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.scoreboard = 0
        self.update_scoreboard()

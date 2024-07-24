from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write(arg=f"Score: {self.scoreboard}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.scoreboard += 1
        self.write(arg=f"Score: {self.scoreboard}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

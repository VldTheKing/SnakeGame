from turtle import Turtle
from datetime import date


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.highest_today_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game over.", align='center', font=('Arial', 24, 'normal'))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_in_file()
        self.score = 0
        self.update_score()

    def write_in_file(self):
        with open("high_score.txt", mode="a") as file:
            file.write(f"High Score: {self.high_score} Date: {date.today()}\n")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

from turtle import *

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align='center', font=("Courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align='center', font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

class Chalk(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.hideturtle()
        self.pensize(13)
        self.penup()

    def draw_field(self):
        self.goto(0, 300)
        self.setheading(270)
        while self.ycor() > -350:
            self.pendown()
            self.forward(70)
            self.penup()
            self.forward(70)

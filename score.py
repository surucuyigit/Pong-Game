from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Arial", 65, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Arial", 65, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update()

    def right_point(self):
        self.right_score += 1
        self.update()

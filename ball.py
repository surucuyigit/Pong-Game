from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = 10
        self.y_movement = 10
        self.left_score = 0
        self.right_score = 0
        self.move_speed = 0.1


    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)


    def change_y(self):
        self.y_movement *= -1

    def change_x(self):
        self.x_movement *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.change_x()





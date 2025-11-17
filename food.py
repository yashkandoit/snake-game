from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.speed(0)

        self.color("blue")
        self.shape("circle")
        self.hunt()

    def hunt(self):
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.goto((random.randint(-280,280),
                   random.randint(-280,280)))

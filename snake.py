from turtle import Turtle


class Snake:

    def __init__(self):
        self.turtles=[]
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            tim=Turtle("square")
            tim.penup()
            tim.setposition((i-1)*20,0)
            tim.color("white")
            self.turtles.append(tim)

    def inc_snake(self):
        tim2=Turtle("square")
        tim2.penup()
        tim2.setposition(self.turtles[0].pos())
        tim2.color("white")
        self.turtles.insert(0,tim2)

    def reset(self):
        for i in self.turtles:
            i.hideturtle()
        self.turtles.clear()
        self.create_snake()

    def move(self):
        for i in range(1,len(self.turtles)):
            self.turtles[i-1].goto(self.turtles[i].pos())
        self.turtles[len(self.turtles)-1].forward(20)

    def up(self):
        if self.turtles[len(self.turtles)-1].heading()!=270:
            self.turtles[len(self.turtles)-1].setheading(90)

    def down(self):
        if self.turtles[len(self.turtles)-1].heading()!=90:
            self.turtles[len(self.turtles)-1].setheading(270)

    def left(self):
        if self.turtles[len(self.turtles)-1].heading()!=0:
            self.turtles[len(self.turtles)-1].setheading(180)

    def right(self):
        if self.turtles[len(self.turtles)-1].heading()!=180:
            self.turtles[len(self.turtles)-1].setheading(0)

    def place(self):
        return self.turtles[len(self.turtles)-1].pos()


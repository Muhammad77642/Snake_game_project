import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.appear()
    def appear(self):
        x=random.randint(-390,390)
        y=random.randint(-390,390)
        self.goto(x,y)


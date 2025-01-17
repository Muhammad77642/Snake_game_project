from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtles = []
        self.positions = [ (-40,0) , (-20, 0), (0, 0),(20, 0),(40,0)]
        self.body()
        self.head=self.turtles[-1]
        self.tail=self.turtles[0]

    def body(self):
        for i in range(len(self.positions)):
            new_snake=Turtle("square")
            new_snake.penup()
            new_snake.goto(self.positions[i])
            new_snake.color("white")
            self.turtles.append(new_snake)
    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)
    def extend(self):
        newpart=Turtle("square")
        newpart.penup()
        newpart.color("white")
        newpart.goto(self.tail.pos())
        self.turtles.insert(0,newpart)


    def right(self):
        self.head.setheading(0)
    def up(self):
        self.head.setheading(90)
    def left(self):
        self.head.setheading(180)
    def down (self):
        self.head.setheading(270)

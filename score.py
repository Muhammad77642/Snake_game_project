from turtle import Turtle
class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0,350)
        self.color("white")
        self.update_score()
    def update_score(self):
        self.write(f"Score:{self.score}",align="center",font=("arial",25,"bold"))
    def increase(self):
        self.score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.clear()
        self.screen.bgcolor("darkred")
        self.write("GAME OVER",align="center",font=("arial",70,"bold"))
        self.goto(0,-100)
        self.write(f"Score:{self.score}",align="center",font=("arial",60,"bold"))



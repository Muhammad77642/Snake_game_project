import time
from score import Score
from snake import Snake
from turtle import Screen
from  food import Food
window=Screen()
window.bgcolor("black")
window.setup(800,800)
hoh=Snake()
window.tracer(0)
food1=Food()
scoree=Score()
game_on=True




while game_on:
    hoh.move()
    window.listen()
    window.onkey(hoh.up, "Up")
    window.onkey(hoh.down, "Down")
    window.onkey(hoh.left, "Left")
    window.onkey(hoh.right, "Right")
    window.update()
    time.sleep(0.1)
    if hoh.head.distance(food1)<20:
            scoree.increase()
            food1.appear()
            hoh.extend()
    if hoh.head.xcor()<= -370 or hoh.head.xcor() >= 370 or    hoh.head.ycor() < -370 or hoh.head.ycor() > 370:
        game_on=False
        scoree.game_over()
    for i in hoh.turtles[:-1]:
        if hoh.head.distance(i)<10:
            game_on=False
            scoree.game_over()

window.exitonclick()

import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake-Game")
screen.tracer(0)


snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game=True
food=Food()
score=Scoreboard()


while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[len(snake.turtles)-1].distance(food)<15:
        food.hunt()
        score.inc_score()
        snake.inc_snake()

    if (snake.turtles[len(snake.turtles)-1].xcor()>280 or snake.turtles[len(snake.turtles)-1].ycor()>280
            or snake.turtles[len(snake.turtles)-1].xcor()<-280 or
            snake.turtles[len(snake.turtles)-1].ycor()<-280):
        score.reset()
        snake.reset()

    for i in range(len(snake.turtles)-2,-1,-1):
        if snake.turtles[len(snake.turtles)-1].distance(snake.turtles[i])<10:
            score.reset()
            snake.reset()
            break

screen.exitonclick()


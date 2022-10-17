from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# Setting up the screen for our game
screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


#Instantiating our snake class
snake=Snake()
#Instantiate food Class
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on =True
while is_game_on:
    screen.update()
    time.sleep(0.1)

# Make our snake to move
    snake.move()
# Detect Collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()



    # Detect Collision with walls

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_game_on=False
        scoreboard.game_over()


    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            scoreboard.game_over()





  





screen.exitonclick()
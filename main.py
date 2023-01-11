from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score


screen = Screen()
screen.bgcolor('black')
screen.setup(width = 500, height = 500)
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
result = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
  time.sleep(0.25)
  screen.update()
  snake.move()
  if snake.snake_len[0].distance(food) < 15:
    food.refresh()
    result.point += 1
    result.score_ref()


    
    
    
  
  
  
 





  
screen.exitonclick()

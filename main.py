from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
from extra import Extra


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
  time.sleep(0.17)
  screen.update()
  snake.move()
      
  if snake.snake_len[0].distance(food) < 15:
    food.refresh()
    result.point += 1
    result.score_ref()
    x = snake.tail.xcor()
    y = snake.tail.ycor()
    extra = Extra()
    extra.goto(x, y)
    snake.snake_len.append(extra)

  for i in range(3, len(snake.snake_len)):
    if snake.snake_len[i].distance(snake.snake_len[0]) < 15:
      game_is_on = False
      result.game_over()


    
    
    
  
  
  
 





  
screen.exitonclick()

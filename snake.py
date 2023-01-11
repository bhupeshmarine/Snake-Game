from turtle import Turtle

class Snake:

  def __init__(self):
    self.snake_len = []
    self.x = -200
    self.y = 0
    self.create_snake()
    self.tail = self.snake_len[-1]
    self.head = self.snake_len[0]

  def create_snake(self):
    for i in range(0,3):
      tim = Turtle("square")
      tim.penup()
      tim.color('white')
      tim.goto(self.x, self.y)
      self.snake_len.append(tim)
      self.x -= 21


  
  def move(self): 
    if self.snake_len[0].xcor() > 225:
      self.head.goto(-225, self.snake_len[0].ycor()) 
    if self.snake_len[0].xcor() < -225:
      self.head.goto(225, self.snake_len[0].ycor())
    if self.snake_len[0].ycor() > 225:
      self.head.goto(self.snake_len[0].xcor(), -225)
    if self.snake_len[0].ycor() < -225:
      self.head.goto(self.snake_len[0].xcor(), 225)
    for i in range(len(self.snake_len)-1, 0, -1):
      a = self.snake_len[i-1].xcor()
      b = self.snake_len[i-1].ycor()
      self.snake_len[i].goto(a, b)
      
    self.snake_len[0].forward(15)
    
  def up(self):
    if self.snake_len[0].heading() != 270:
      self.snake_len[0].setheading(90)

  def down(self):
    if self.snake_len[0].heading() != 90:
      self.snake_len[0].setheading(270)
      
  def left(self):
    if self.snake_len[0].heading() != 0:
      self.snake_len[0].setheading(180)
      
  def right(self):
    if self.snake_len[0].heading() != 180:
      self.snake_len[0].setheading(0)

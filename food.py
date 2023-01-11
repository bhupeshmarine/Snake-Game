from turtle import Turtle
import random
class Food(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('red')
    self.refresh()
    

  def refresh(self):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    self.penup()
    self.goto(x, y)
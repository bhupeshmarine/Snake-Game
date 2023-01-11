from turtle import Turtle

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color("white")
    self.point = 0
    self.goto(0, 220)
    self.hideturtle()
    self.score_ref()
    
    

  def score_ref(self):
    self.clear()
    self.write(arg = f"Score: {self.point}", align = "center", font=('Arial', 12, 'normal'))

  def game_over(self):
    self.goto(0, 0)
    self.color('red')
    self.write(arg = "Game Over", align = "center", font=('Arial', 15, 'bold'))

from turtle import Turtle

class Scoreboard(Turtle):
   
    def __init__(self):
      super().__init__()
      self.color('white')
      self.penup()
      self.hideturtle()
      self.l_score = 0
      self.r_score = 0
      self.update()
    
    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def plus_left(self):
      self.clear()
      self.l_score += 1
      self.update()


    def plus_right(self):
      self.clear()
      self.r_score += 1
      self.update()
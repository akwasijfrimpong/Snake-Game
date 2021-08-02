from turtle import Turtle

class Score(Turtle):

    def __init__(self, score=0):
        super().__init__()
        self.penup()
        self.high_score = 0
        self.score = 0
        self.hideturtle()
        self.score = score
        self.goto(0,270)
        self.color('white')
        self.speed("fastest")
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.write(f"SCORE: {score} High Score: {self.high_score}", align='center',font=("Arial",16,'normal'))


    def update_score(self, score):
        self.score = score
        self.clear()
        self.write(f"SCORE: {score} High Score: {self.high_score}", align='center', font=("Arial", 16, 'normal'))

    def reset(self,track):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score= 0
        self.update_score(self.score)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align="center", font=("Arial", 16, 'normal'))
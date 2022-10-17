from turtle import Turtle
ALIGNMENT ="center"
FONT =('Ariel', 12, 'normal')
class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        #function called below helps to update scores
        self.update_scorebord()


    #This function writes the scores on the screen
    def update_scorebord(self):
        self.write(f"Score={self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)



    #This function increase the scores
    def increase_score(self):
        self.score +=1
        #The line of code below ensures the scores are not overlapping
        self.clear()
        self.update_scorebord()



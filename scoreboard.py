from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))
        self.goto(100, 270)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 18, "normal"))

    def yellow_point(self):
        self.score += 1
        self.update_scoreboard()

    def green_point(self):
        self.score += 3
        self.update_scoreboard()

    def orange_point(self):
        self.score += 5
        self.update_scoreboard()

    def red_point(self):
        self.score += 7
        self.update_scoreboard()

    def lost(self):
        self.lives -= 1
        self.update_scoreboard()

    def gameover(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAMEOVER", align="center", font=("Courier", 50, 'bold'))
        self.goto(0, -100)
        self.write(f"Final Score: {self.score}", align='center', font=("Courier", 24, "normal"))

    def win(self):
        self.clear()
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Courier", 50, 'bold'))
        self.goto(0, -100)
        self.write(f"Final Score: {self.score}", align='center', font=("Courier", 24, "normal"))

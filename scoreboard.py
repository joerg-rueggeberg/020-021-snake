from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 9, "normal")
FONT2 = ("Verdana", 10, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.pu()
        self.hideturtle()
        self.setpos(x=0, y=280)
        self.write(f"Score: {self.score} - Highscore: {self.high_score}", False, ALIGNMENT, FONT)

    def add(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} - Highscore: {self.high_score}", False, ALIGNMENT, FONT)

    def reset_score(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as data:
                data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} - Highscore: {self.high_score}", False, ALIGNMENT, FONT)
        return True

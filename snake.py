from turtle import Turtle
COORD_START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20


class Snake:
    def __init__(self):
        self.snakes = []
        self.start()
        self.head = self.snakes[0]

    def start(self):
        for coord in COORD_START:
            self.add_segment(coord)

    def add_segment(self, position):
        seg = Turtle()
        seg.shape("square")
        seg.color("white")
        seg.pu()
        seg.setpos(position)
        self.snakes.append(seg)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            # vorheriges Segment wird neues Ziel
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            # nachfolgendes Segment geht zur Position vom vorherigen
            self.snakes[snake].goto(new_x, new_y)
        # erstes Segment geht vor
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset_snake(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.start()
        self.head = self.snakes[0]

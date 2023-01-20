from turtle import Turtle
POSITIONS = [(-350, 0), (350, 0)]


class Rackets(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create()
        self.head = self.segments[0]
        self.head2 = self.segments[1]

    def create(self):
        for position in POSITIONS:
            self.create_racket(position)

    def create_racket(self, position):
        racket = Turtle("square")
        racket.color("white")
        racket.shapesize(stretch_wid=5, stretch_len=1)
        racket.penup()
        racket.goto(position)
        self.segments.append(racket)

    def l_go_up(self):
        new_y = self.head.ycor() + 20
        self.head.goto(self.head.xcor(), new_y)

    def l_go_down(self):
        new_y = self.head.ycor() - 20
        self.head.goto(self.head.xcor(), new_y)

    def r_go_up(self):
        new_y = self.head2.ycor() + 20
        self.head2.goto(self.head2.xcor(), new_y)

    def r_go_down(self):
        new_y = self.head2.ycor() - 20
        self.head2.goto(self.head2.xcor(), new_y)

from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20


class Snake:


    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in STARTING_POSITION:
            turt = Turtle(shape="square")
            turt.color("white")
            turt.penup()
            turt.goto(i)
            self.segments.append(turt)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        for i in STARTING_POSITION:
            self.add_segment(self.segments[-1].position())

    def add_segment(self,i):
        turt = Turtle(shape="square")
        turt.color("white")
        turt.penup()
        turt.goto(i)
        self.segments.append(turt)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)


    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)

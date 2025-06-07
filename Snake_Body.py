from turtle import Turtle

starting_positions = [(0,0), (-10,0), (-20,0)]
Distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
       self.snakes = []
       self.create_snake()
       self.head = self.snakes[0] 

    def create_snake(self):
        for position in starting_positions:
            self.add_part(position)

    def add_part(self, position):
        snake = Turtle()
        snake.shape('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)
    
    def extend(self):
        self.add_part(self.snakes[-1].position())
        

    def move(self):
        for one in range(len(self.snakes)-1, 0, -1):
            x = self.snakes[one - 1].xcor()
            y = self.snakes[one - 1].ycor()
            self.snakes[one].goto(x, y)
        self.head.forward(Distance)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
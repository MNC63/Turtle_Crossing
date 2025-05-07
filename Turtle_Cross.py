from turtle import Turtle, Screen

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
STARTING_X = 0
STARTING_Y = -250



class Cross(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow")
        self.goto(STARTING_X, STARTING_Y)
        self.setheading(90)

    def Up(self):
        y_pos = self.ycor() +10
        self.goto(self.xcor(), y_pos)
    
    def Down(self):
        y_pos= self.ycor() -10
        self.goto(self.xcor(), y_pos)

    def Right(self):
        x_pos = self.xcor() +10
        self.goto(x_pos, self.ycor())
    
    def Left(self):
        x_pos = self.xcor() -10
        self.goto(x_pos, self.ycor())


display = Screen()
display.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
display.bgcolor("black")
display.title("Turtle Cross")
display.tracer(0)



turtle_cross = Cross()

display.listen()
display.onkey(turtle_cross.Up, "w")
display.onkey(turtle_cross.Down, "s")
display.onkey(turtle_cross.Right, "d")
display.onkey(turtle_cross.Left, "a")

Start_cross = True
while Start_cross:
    display.update()


display.exitonclick()
# display.mainloop()


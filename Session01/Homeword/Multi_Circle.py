import turtle
myTurtle = turtle.Turtle(shape = "turtle")
myTurtle.color("black")
myTurtle.speed(-1)

for i in range(1000):
    myTurtle.forward(0.5)
    myTurtle.left(7)
    myTurtle.circle(100)

turtle.getscreen().mainloop()
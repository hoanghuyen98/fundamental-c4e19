import turtle
 
myTurtle = turtle.Turtle(shape = "turtle")
myTurtle.color("green", "black")
myTurtle.begin_fill()

myTurtle.circle(100)

myTurtle.end_fill()
turtle.getscreen().mainloop()
from turtle import *

shape("turtle")
color("black")
speed(-1)
soCanh = int(input("How much edge you want : "))
print("Number of side: ", soCanh)
for i in range(soCanh) :
    forward(100)
    left(360 / soCanh)
    

mainloop()

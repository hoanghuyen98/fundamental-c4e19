from turtle import*
shape("turtle")
color("green")
bgcolor("black")
speed(-1)
edge = 2
for i in range(7):
    edge +=1
    for j in range(edge):
        forward(100)
        left(360/edge)
    if(edge%2==0):
        color("green")
    else:
        color("red")    
   

mainloop()
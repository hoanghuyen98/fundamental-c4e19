from turtle import*
shape = "turtle"
speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5):
    for j in range(1):
        begin_fill()
        color(colors[i])
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)       
        end_fill()
        forward(100)
        
        
mainloop()
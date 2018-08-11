from turtle import*
shape("turtle")
# speed(-1)
colors = ["red", "blue", "brown", "yellow", "grey"]
edge = 3
for i in range (5):
    for j in range(edge):
        color(colors[i])
        forward(100)
        left(360/edge)
        
    edge += 1    

mainloop()
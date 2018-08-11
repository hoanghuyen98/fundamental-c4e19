from turtle import*
import random
shape("turtle")
colors = ['red', 'green', 'blue', 'white', 'yellow', 'pink', 'purple', 'orange']
bgcolor("black")
size = 1
speed(-1)
for i in range(100):
    for j in range(4):
        color(random.choice(colors))
        forward(size)
        left(90)
    left(5)
    size = size+3
    color(random.choice(colors))
    
mainloop()
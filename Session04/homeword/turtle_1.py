from turtle import*
import random
colors = ['blue', 'orange', 'purple', 'white','yellow','red','pink','green']
shape("turtle")
speed(-1)
bgcolor("black")

for i in range(24):
    for j in range(4):
        color(random.choice(colors))
        forward(100)
        left(90)
    left(15)
    color(random.choice(colors))

# end_fill()

mainloop()
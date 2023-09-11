#sample codes:
#these codes do NOT work on the spirit machine

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(1,18):
    alex.forward(10*i)
    alex.left(90)

wn.mainloop()
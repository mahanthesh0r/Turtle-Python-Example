import turtle as t

start = 1
previous = 0
fibo = None

t.bgcolor('black')

color = ['red','white','blue']

for i in range(13):
    fibo = start + previous
    t.pencolor(color[i%3])
    t.circle(fibo,180)

    previous = start
    start = fibo

t.mainloop()

import turtle as t

sides = int(input('Enter an odd positive integer: '))

if sides % 2 == 0:
    print('Wrong Input! Please enter a correct value')
    exit()
else:
    angle = 360 / sides
    for count in range(sides):
        t.fd(50)
        t.lt(angle)

t.mainloop()

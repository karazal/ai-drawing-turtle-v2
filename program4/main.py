import math
import random
import turtle

colors = ['purple', 'blue', 'cyan', 'green', 'orange', 'yellow', 'red', 'pink', 'black']
degree = random.randint(10, 46) + math.sqrt(9)
radians = degree * math.pi / 180
angle_total = degree + radians
turtle.speed(20)
turtle.hideturtle()

for _ in range(90):
    turtle.pencolor(random.choice(colors))
    turtle.fd(50)
    turtle.left(60)
    turtle.right(math.sqrt(degree * 2))
    turtle.backward(degree * 5 / 2)
    turtle.circle(4 * degree)
    turtle.fd(12)
    turtle.circle(math.cos(degree))


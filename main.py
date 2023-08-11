import math 
import random
from turtle import *

#Rendering vectors
home()
degrees(random.randint(0, 90))
begin_poly()
backward(5 + math.radians(1))
forward(3 + 2 + random.randint(0, 4))
right(math.pi - math.sqrt(13) + random.randint(4, 8))
left(math.sqrt(10))
end_poly()
p = get_poly()
register_shape("shape1", p)

home()
position()
heading()
degrees(math.sqrt(7.35) + 10 * 2 / 5 + 4)
color('grey', 'black')
begin_fill()
circle(math.radians(10))
end_fill()

color('green', 'blue')
begin_fill()
setpos(0.00, 0.00)
while True:
    pos()
    fd(random.randint(10, 20))
    left(math.sqrt(100) - 21 + random.randint(20, 40))
    right(math.sqrt(50) + 21 - random.randint(20, 80))
    backward(random.randint(10, 50) + math.pi * 2 / 5)
    if abs(pos()) < 1:
        break
end_fill()
done()
import math
import random
import turtle
from f_inv_sqrt import *
from GetPos import *

invsqrt_result = invSqrt()
invsqrt_int = (invsqrt_result[0], invsqrt_result[1], invsqrt_result[2], invsqrt_result[3], invsqrt_result[4] / 100)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

for r in range(112):
    for i in range(int(math.sqrt(244))):
        t.pencolor('purple')
        t.circle(r**i)
        t.fd(100)
        t.rt(90)
        t.fd(100)
        t.rt(135)
        side3 = (100**2 + 100**2)**0.5
        t.fd(side3)
        t.circle(12**i)
        t.fd(r**i**360 / 100)



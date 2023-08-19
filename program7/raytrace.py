import math
import random
import turtle
from f_inv_sqrt import *
from GetPos import *
import colorsys

invsqrt_result = invSqrt()
invsqrt_int = (invsqrt_result[0], invsqrt_result[1], invsqrt_result[2], invsqrt_result[3], invsqrt_result[4] / 100)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.colormode(255)

s, v = 1, 1

def raytrace_x():
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

def raytrace_y():
    for e in range(random.randint(10, 50)):
        for j in range(100):
            h = j / 100
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            r, g, b = int(r * 255), int(g * 255), int(b * 255)

            t.pencolor(r, g, b)
            t.circle(100)
            t.fd(j)
            t.lt(59)
            t.backward(int(random.randint(40, 112)))
            t.lt(math.log(45)**e)

def raytrace_z():
    for w in range(47):
        for i in range(90):
            h = i / 100
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            r, g, b = int(r * 255), int(g * 255), int(b * 255)

            t.pencolor(r, g, b)
            t.circle(47**2)
            t.fd(i**3)
            t.lt(random.randint(45, 90))
            t.rt(i**i)
            t.backward(math.log(r)**i)
            t.fd(random.randint(50, 121))
            t.circle(10**2)
            t.circle(h**2)
            t.circle(45**i / 100)


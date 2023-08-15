import turtle as tur
import colorsys
from f_inv_sqrt import *

#start
t = tur.Turtle()
tur.screensize(800, 600)
t.speed(0)
tur.speed(0)
t.hideturtle()
tur.hideturtle()

start_hue = 0.5
end_hue = 1 
num_steps = 10 
hue_step = (end_hue - start_hue) / num_steps

invsqrt_result = invSqrt()
invsqrt_int = int(invsqrt_result[0] + invsqrt_result[1] + invsqrt_result[2] + invsqrt_result[3] + invsqrt_result[4] / 100)
for k in range(90):
    for j in range(30):
        for i in range(num_steps + 1):
            hue = start_hue + i * hue_step
            rgb = colorsys.hsv_to_rgb(hue, 1, 1)
            tur.pencolor(*rgb)
            tur.fd(k)
            tur.lt(j**3)
            t.pencolor(*rgb)
            tur.circle(k**j)
            t.fd(100)
            t.rt(90)
            t.fd(100)
            t.rt(135)
            side3 = (100**2 + 100**2)**0.5
            tur.fd(side3)
            tur.circle(12**j)
            t.circle(j**i)
            t.circle(k**3)
            t.fd(50)
            t.rt(30)
            t.fd(50)
            t.rt(int(135 / 2))


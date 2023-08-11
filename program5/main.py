import random as r
import colorsys
import turtle as tur
import math 

R_COORD = r.randint(50, 76)
G_COORD = r.randint(20, 80)
B_COORD = r.randint(10, 45)

#Start
tur.speed(0)
tur.home()
tur.pos()
tur.fd(r.randint(10, 100))
tur.circle(24)
for i in range(100):
    for c in ('purple', 'blue', 'cyan', 'green', 'lime', 'orange', 'yellow', 'red', 'pink' ):
        tur.begin_fill()
        tur.color(c)  
        tur.fd(25)
        tur.lt(R_COORD)
        tur.backward(112)
        tur.rt(30)
        tur.end_fill()

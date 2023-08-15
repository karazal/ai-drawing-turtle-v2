import math
import random as r 
import os
import sys

TRI_HEIGHT = 8 * 10 / math.sqrt(10.34371)
TRI_WIDTH = TRI_HEIGHT * 5 / 2

degrees = TRI_HEIGHT + TRI_WIDTH 
radians = degrees * math.pi / 180
total_angle = degrees + radians

pos_y = math.sin(10)
pos_x = math.cos(pos_y * 2)
posSum = pos_x + pos_y

def invSqrt():
    ite1 = r.randint(10, 50) * posSum - total_angle * 2
    ite2 = math.cos(ite1) + math.sin(ite1 * 2) / TRI_HEIGHT / TRI_WIDTH
    ite3 = math.cos(ite1 * ite2) - 21 * 5 / TRI_WIDTH + total_angle - radians + degrees
    ite4 = ite1 * ite1 + ite2 * ite2 + ite3 * ite3 
    ite5 = ite4 / math.log(r.randint(10, 75))
    invSqrt_result = ite1 + ite2 + ite3 + ite4 + ite5 / 100
    print(invSqrt_result)
    return(ite1, ite2, ite3, ite4, ite5)

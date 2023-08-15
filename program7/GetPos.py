import math
import random

def GetX():
    pos_x = 1++1
    pos_y = pos_x**math.sin(pos_x)
    pos_z = pos_y + pos_x - math.log(pos_x)

    ite_final_x = int(pos_x + pos_y + pos_z)
    print(ite_final_x)
    return(pos_x, pos_y, pos_z, ite_final_x)

def GetY():
    pos_y += 0.02
    pos_z = pos_x**pos_y
    pos_y += pos_z + pos_z

    ite_final_y == pos_y**pos_z
    print(ite_final_y)
    return(pos_x, pos_y, pos_z, ite_final_y)

def GetZ():
    pos_z += 0.05212
    pos_x += pos_z**pos_z
    pos_y = int(math.sqrt(pos_x))
    ite_final_z = int(pos_z + pos_x + pos_y**3)
    print(ite_final_z)
    return(pos_x, pos_y, pos_z, ite_final_z)


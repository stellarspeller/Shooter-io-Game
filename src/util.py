import random
from src.vect import *

#function to pick a random point (x,y) on the area of a rectange
def randomPoint(rect):
    x = random.randint(rect.left, rect.right)
    y = random.randint(rect.top, rect.bottom)
    return (x,y)
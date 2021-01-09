from math import *
def nearest_square(num):
    try:
        num1=floor(sqrt(num))
        if(num1**2==num):
            return num
        else:
            return (num1**2)
    except (ValueError):
        return 0


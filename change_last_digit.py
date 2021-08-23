import math

def change_digit(nr: float):
    nr = str(nr)
    digits_after_point = nr.split(".")[1]
    
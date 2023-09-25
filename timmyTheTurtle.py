from turtle import *
from random import random

def go_top_left():
    """position cursor in top left of picture"""
    up()
    goto(-500, 300)
    rt(90)
    down()

def draw_background_box():
    """draw a background/sky box"""
    go_top_left()
    fillcolor("skyblue")
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(600)
        else:
            fd(1000)
        lt(90)
    end_fill()

def main():
    draw_background_box()

draw_background_box()

mainloop()

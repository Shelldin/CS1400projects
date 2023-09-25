from turtle import *
from random import random

bg_x_length = 1200
bg_y_length = 800


def go_top_left():
    """position cursor in top left of picture"""
    up()
    goto(bg_x_length / -2, bg_y_length / 2)
    down()


def go_bottom_left():
    """position cursor in bottom left of picture"""
    up()
    goto(bg_x_length / -2, bg_y_length / -2)
    down()


def go_bottom_center():
    """position cursor in bottom middle of picture"""
    up()
    goto(0, bg_y_length / -2)
    down()


def draw_background_box():
    """draw a background/sky box"""
    go_top_left()
    setheading(270)
    fillcolor("skyblue")
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(bg_y_length)
        else:
            fd(bg_x_length)
        lt(90)
    end_fill()


def draw_doorway():
    count = 0
    door_x_length = 150
    door_y_length = 250
    go_bottom_center()
    fillcolor("black")
    seth(0)
    up()
    fd(door_x_length / 2)
    down()
    seth(90)
    begin_fill()
    while count < 4:
        if count % 2 == 0:
            fd(door_y_length)
        else:
            fd(door_x_length)
        count += 1
        lt(90)
    end_fill()


# variables for the pillar functions
pillar_long_x_length = 100
pillar_short_x_length = 50
pillar_y_length = 300


def draw_pillar_base():
    """draw the base of a pillar"""
    fillcolor("ivory1")
    begin_fill()
    fd(pillar_long_x_length)
    goto(xcor() - (pillar_long_x_length * .25), ycor() + (pillar_long_x_length * .5))
    goto(xcor() - pillar_short_x_length, ycor())
    goto(xcor() - (pillar_long_x_length * .25), ycor() - (pillar_long_x_length * .5))
    end_fill()
    # TEMPORARY
    up()
    goto(xcor() + (pillar_long_x_length * .25), ycor() + (pillar_long_x_length * .5))
    down()


def draw_pillar_column():
    """Draw the main section of the pillar"""
    seth(90)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(pillar_y_length)
        else:
            fd(pillar_short_x_length)
        rt(90)
    end_fill()


def main():
    draw_background_box()
    draw_doorway()
    rt(90)
    fd(25)
    draw_pillar_base()
    draw_pillar_column()


main()

mainloop()

from turtle import *
from random import random

# background dimension variables
bg_x_length = 1400
bg_y_length = 800

# door dimension variables
door_x_length = 150
door_y_length = 250

# variables for the pillar functions
pillar_long_x_length = 100
pillar_short_x_length = 50
pillar_y_length = 300
pillar_base_y_length = pillar_long_x_length / 2
pillar_total_height = pillar_y_length + pillar_base_y_length * 2

# base building variables
main_building_x_length = door_x_length + 200 + (pillar_long_x_length * 8)
main_building_y_length = pillar_total_height


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
    """draw the doorway shape"""
    count = 0
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


def draw_pillar_base():
    """draw the base of a pillar"""
    begin_fill()
    fd(pillar_long_x_length)
    goto(xcor() - (pillar_long_x_length * .25), ycor() + pillar_base_y_length)
    goto(xcor() - pillar_short_x_length, ycor())
    goto(xcor() - (pillar_long_x_length * .25), ycor() - pillar_base_y_length)
    end_fill()
    up()
    goto(xcor() + (pillar_long_x_length * .25), ycor() + pillar_base_y_length)
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
    fd(pillar_y_length)


def draw_pillar_top():
    seth(0)
    begin_fill()
    fd(pillar_short_x_length)
    goto(xcor() + (pillar_long_x_length * .25), ycor() + pillar_base_y_length)
    goto(xcor() - pillar_long_x_length, ycor())
    goto(xcor() + (pillar_long_x_length * .25), ycor() - pillar_base_y_length)
    end_fill()


def draw_all_pillars():
    pillar_count = 8
    fillcolor("ivory1")
    go_bottom_center()
    seth(0)
    up()
    fd(door_x_length / 2)

    # draw the right side pillars
    while pillar_count > 4:
        seth(0)
        fd(25)
        down()
        draw_pillar_base()
        draw_pillar_column()
        draw_pillar_top()
        up()
        goto(xcor() + pillar_short_x_length + (pillar_long_x_length * .25), bg_y_length / -2)
        pillar_count -= 1

    go_bottom_center()
    seth(180)
    up()
    fd((door_x_length / 2) + 125 + (pillar_long_x_length * 4))

    # draw left side pillars
    while pillar_count > 0 and pillar_count < 5:
        seth(0)
        fd(25)
        down()
        draw_pillar_base()
        draw_pillar_column()
        draw_pillar_top()
        up()
        goto(xcor() + pillar_short_x_length + (pillar_long_x_length * .25), bg_y_length / -2)
        pillar_count -= 1


def draw_main_pantheon_walls():
    """draw the main building walls of the pantheon"""
    go_bottom_center()
    fillcolor("ivory4")
    up()
    goto(main_building_x_length / -2, ycor())
    down()
    seth(0)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(main_building_x_length)
        else:
            fd(main_building_y_length)
        lt(90)
    end_fill()

def draw_roof_rectangles():
    fillcolor("ivory1")
    go_bottom_center()
    up()
    goto((main_building_x_length / -2) - 15, ycor() + main_building_y_length)
    down()
    seth(0)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(main_building_x_length + 30)
        else:
            fd(15)
        lt(90)
    end_fill()

    fillcolor("ivory2")
    up()
    goto(xcor() + 15, ycor() + 15)
    down()

    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(main_building_x_length)
        else:
            fd(30)
        lt(90)
    end_fill()

def main():
    #draw_background_box()
    draw_main_pantheon_walls()
    #draw_doorway()
    #draw_all_pillars()
    draw_roof_rectangles()


main()

mainloop()

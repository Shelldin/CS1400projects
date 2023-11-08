from turtle import *

# size factor
factor_amount = 1

# background dimension variables
bg_x_length = 1400
bg_y_length = 850

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

# upper roof dimension variables
upper_roof_x_length = door_x_length + 150 + (pillar_long_x_length * 8)
upper_roof_y_length = pillar_total_height / 3


def go_top_left(bg_x_length, bg_y_length, factor_amount):
    """position cursor in top left of picture"""
    up()
    goto((bg_x_length * factor_amount) / -2, (bg_y_length * factor_amount) / 2)
    down()


def go_bottom_left(bg_x_length, bg_y_length, factor_amount):
    """position cursor in bottom left of picture"""
    up()
    goto((bg_x_length * factor_amount) / -2, (bg_y_length * factor_amount) / -2)
    down()


def go_bottom_center(bg_y_length, factor_amount):
    """position cursor in bottom middle of picture"""
    up()
    goto(0, (bg_y_length * factor_amount) / -2)
    down()


def draw_background_box(bg_x_length, bg_y_length, factor_amount):
    """draw a background/sky box"""
    go_top_left(bg_x_length, bg_y_length, factor_amount)
    setheading(270)
    fillcolor("skyblue")
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(bg_y_length * factor_amount)
        else:
            fd(bg_x_length * factor_amount)
        lt(90)
    end_fill()


def draw_doorway(bg_x_length, bg_y_length, factor_amount):
    """draw the doorway shape"""
    count = 0
    go_bottom_center(bg_y_length, factor_amount)
    fillcolor("black")
    seth(0)
    up()
    fd((door_x_length * factor_amount) / 2)
    down()
    seth(90)
    begin_fill()

    while count < 4:
        if count % 2 == 0:
            fd(door_y_length * factor_amount)
        else:
            fd(door_x_length * factor_amount)
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
    while 0 < pillar_count < 5:
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

    fillcolor("ivory1")
    up()
    goto(xcor() - 15, ycor() + 30)
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


def draw_upper_roof():
    go_bottom_center()
    fillcolor("ivory3")
    up()
    goto(xcor() + (upper_roof_x_length / -2), ycor() + pillar_total_height + 60)
    down()
    seth(0)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(upper_roof_x_length)
        else:
            fd(upper_roof_y_length)
        lt(90)
    end_fill()

    fillcolor("ivory2")
    up()
    goto((xcor() - 15, ycor() + upper_roof_y_length))
    down()
    seth(0)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(upper_roof_x_length + 30)
        else:
            fd(15)
        lt(90)
    end_fill()


def draw_roof_triangles():
    fillcolor("ivory1")
    tri_start_pos = pos()
    tri_side_count = 0
    seth(0)
    down()
    begin_fill()
    while tri_side_count < 3:
        if tri_side_count == 0:
            goto(0, ycor() + 120)
            tri_side_count += 1
        elif tri_side_count == 1:
            goto(tri_start_pos)
            seth(0)
            fd(main_building_x_length + 30)
            tri_side_count += 1
        elif tri_side_count == 2:
            goto(0, ycor() + 120)
            tri_side_count += 1
        else:
            break
    end_fill()

    fillcolor("ivory2")
    up()
    goto(tri_start_pos)
    goto(xcor() + 70, ycor())
    second_tri_start_pos = pos()
    tri_side_count = 0
    down()
    begin_fill()
    while tri_side_count < 3:
        if tri_side_count == 0:
            goto(0, ycor() + 100)
            tri_side_count += 1
        elif tri_side_count == 1:
            goto(second_tri_start_pos)
            seth(0)
            fd(main_building_x_length - 120)
            tri_side_count += 1
        elif tri_side_count == 2:
            goto(0, ycor() + 100)
            tri_side_count += 1
        else:
            break
    end_fill()


def draw_dome():
    fillcolor("ivory2")
    up()
    goto(0, ycor() + upper_roof_y_length + 30)
    goto(xcor() - 220, ycor())
    down()
    seth(90)
    begin_fill()
    for i in range(181):
        fd(4)
        seth(89 - i)
    end_fill()


def draw_roof():
    draw_roof_rectangles()
    roof_left_edge = pos()
    draw_upper_roof()
    up()
    goto(roof_left_edge)
    goto(xcor(), ycor() + 15)
    draw_roof_triangles()
    up()
    goto(roof_left_edge)
    draw_dome()


def main():
    draw_background_box()
    draw_main_pantheon_walls()
    draw_doorway()
    draw_all_pillars()
    draw_roof()


main()

mainloop()

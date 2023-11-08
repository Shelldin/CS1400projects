from turtle import *


def go_top_left(bg_x_length, bg_y_length):
    """position cursor in top left of picture"""
    up()
    goto(bg_x_length / -2, bg_y_length / 2)
    down()


def go_bottom_left(bg_x_length, bg_y_length):
    """position cursor in bottom left of picture"""
    up()
    goto(bg_x_length / -2, bg_y_length / -2)
    down()


def go_bottom_center(bg_y_length):
    """position cursor in bottom middle of picture"""
    up()
    goto(0, bg_y_length / -2)
    down()


def draw_background_box(bg_x_length, bg_y_length):
    """draw a background/sky box"""
    go_top_left(bg_x_length, bg_y_length)
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


def draw_doorway(bg_y_length, door_x_length, door_y_length):
    """draw the doorway shape"""
    count = 0
    go_bottom_center(bg_y_length)
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


def draw_pillar_base(pillar_long_x_length, pillar_short_x_length, pillar_base_y_length):
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


def draw_pillar_column(pillar_y_length, pillar_short_x_length):
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


def draw_pillar_top(pillar_short_x_length, pillar_long_x_length, pillar_base_y_length):
    seth(0)
    begin_fill()
    fd(pillar_short_x_length)
    goto(xcor() + (pillar_long_x_length * .25), ycor() + pillar_base_y_length)
    goto(xcor() - pillar_long_x_length, ycor())
    goto(xcor() + (pillar_long_x_length * .25), ycor() - pillar_base_y_length)
    end_fill()


def draw_all_pillars(door_x_length, bg_y_length, pillar_short_x_length, pillar_long_x_length, pillar_y_length,
                     pillar_base_y_length, factor_amount):
    pillar_count = 8
    fillcolor("ivory1")
    go_bottom_center(bg_y_length)
    seth(0)
    up()
    fd(door_x_length / 2)

    # draw the right side pillars
    while pillar_count > 4:
        seth(0)
        fd(25 * factor_amount)
        down()
        draw_pillar_base(pillar_long_x_length, pillar_short_x_length, pillar_base_y_length)
        draw_pillar_column(pillar_y_length, pillar_short_x_length)
        draw_pillar_top(pillar_short_x_length, pillar_long_x_length, pillar_base_y_length)
        up()
        goto(xcor() + pillar_short_x_length + (pillar_long_x_length * .25),
             bg_y_length / -2)
        pillar_count -= 1

    go_bottom_center(bg_y_length)
    seth(180)
    up()
    fd((door_x_length / 2) + (125 * factor_amount) + (pillar_long_x_length * 4))

    # draw left side pillars
    while 0 < pillar_count < 5:
        seth(0)
        fd(25 * factor_amount)
        down()
        draw_pillar_base(pillar_long_x_length, pillar_short_x_length, pillar_base_y_length)
        draw_pillar_column(pillar_y_length, pillar_short_x_length)
        draw_pillar_top(pillar_short_x_length, pillar_long_x_length, pillar_base_y_length)
        up()
        goto(xcor() + pillar_short_x_length + (pillar_long_x_length * .25), bg_y_length / -2)
        pillar_count -= 1


def draw_main_pantheon_walls(bg_y_length, main_building_x_length, main_building_y_length):
    """draw the main building walls of the pantheon"""
    go_bottom_center(bg_y_length)
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


def draw_roof_rectangles(bg_y_length, main_building_x_length, main_building_y_length, factor_amount):
    fillcolor("ivory1")
    go_bottom_center(bg_y_length)
    up()
    goto((main_building_x_length / -2) - 15, ycor() + main_building_y_length)
    down()
    seth(0)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(main_building_x_length + (30 * factor_amount))
        else:
            fd(15 * factor_amount)
        lt(90)
    end_fill()

    fillcolor("ivory2")
    up()
    goto(xcor() + (15 * factor_amount), ycor() + (15 * factor_amount))
    down()

    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(main_building_x_length)
        else:
            fd(30 * factor_amount)
        lt(90)
    end_fill()

    fillcolor("ivory1")
    up()
    goto(xcor() - (15 * factor_amount), ycor() + (30 * factor_amount))
    down()
    seth(0)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(main_building_x_length + (30 * factor_amount))
        else:
            fd(15 * factor_amount)
        lt(90)
    end_fill()


def draw_upper_roof(bg_y_length, upper_roof_x_length, upper_roof_y_length, pillar_total_height, factor_amount):
    go_bottom_center(bg_y_length)
    fillcolor("ivory3")
    up()
    goto(xcor() + (upper_roof_x_length / -2), ycor() + pillar_total_height + (60 * factor_amount))
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
    goto((xcor() - (15 * factor_amount), ycor() + upper_roof_y_length))
    down()
    seth(0)
    begin_fill()
    for i in range(4):
        if i % 2 == 0:
            fd(upper_roof_x_length + (30 * factor_amount))
        else:
            fd(15 * factor_amount)
        lt(90)
    end_fill()


def draw_roof_triangles(main_building_x_length, factor_amount):
    fillcolor("ivory1")
    tri_start_pos = pos()
    tri_side_count = 0
    seth(0)
    down()
    begin_fill()
    while tri_side_count < 3:
        if tri_side_count == 0:
            goto(0, ycor() + (120 * factor_amount))
            tri_side_count += 1
        elif tri_side_count == 1:
            goto(tri_start_pos)
            seth(0)
            fd(main_building_x_length + (30 * factor_amount))
            tri_side_count += 1
        elif tri_side_count == 2:
            goto(0, ycor() + (120 * factor_amount))
            tri_side_count += 1
        else:
            break
    end_fill()

    fillcolor("ivory2")
    up()
    goto(tri_start_pos)
    goto(xcor() + (70 * factor_amount), ycor())
    second_tri_start_pos = pos()
    tri_side_count = 0
    down()
    begin_fill()
    while tri_side_count < 3:
        if tri_side_count == 0:
            goto(0, ycor() + (100 * factor_amount))
            tri_side_count += 1
        elif tri_side_count == 1:
            goto(second_tri_start_pos)
            seth(0)
            fd(main_building_x_length - (120 * factor_amount))
            tri_side_count += 1
        elif tri_side_count == 2:
            goto(0, ycor() + (100 * factor_amount))
            tri_side_count += 1
        else:
            break
    end_fill()


def draw_dome(upper_roof_y_length, factor_amount):
    fillcolor("ivory2")
    up()
    goto(0, ycor() + upper_roof_y_length + (30 * factor_amount))
    goto(xcor() - (220 * factor_amount), ycor())
    down()
    seth(90)
    begin_fill()
    for i in range(181):
        fd(4)
        seth(89 - i)
    end_fill()


def draw_roof(bg_y_length, main_building_x_length, main_building_y_length, upper_roof_x_length, upper_roof_y_length,
              pillar_total_height, factor_amount):
    draw_roof_rectangles(bg_y_length, main_building_x_length, main_building_y_length, factor_amount)
    roof_left_edge = pos()
    draw_upper_roof(bg_y_length, upper_roof_x_length, upper_roof_y_length, pillar_total_height, factor_amount)
    up()
    goto(roof_left_edge)
    goto(xcor(), ycor() + (15 * factor_amount))
    draw_roof_triangles(main_building_x_length, factor_amount)
    up()
    goto(roof_left_edge)
    draw_dome(upper_roof_y_length, factor_amount)


def main():
    # size factor
    factor_amount = .5

    # background dimension variables
    bg_x_length = 1400 * factor_amount
    bg_y_length = 850 * factor_amount

    # door dimension variables
    door_x_length = 150 * factor_amount
    door_y_length = 250 * factor_amount

    # variables for the pillar functions
    pillar_long_x_length = 100 * factor_amount
    pillar_short_x_length = 50 * factor_amount
    pillar_y_length = 300 * factor_amount
    pillar_base_y_length = pillar_long_x_length / 2
    pillar_total_height = pillar_y_length + pillar_base_y_length * 2

    # base building variables
    main_building_x_length = door_x_length + (200 * factor_amount) + (pillar_long_x_length * 8)
    main_building_y_length = pillar_total_height

    # upper roof dimension variables
    upper_roof_x_length = door_x_length + (150 * factor_amount) + (pillar_long_x_length * 8)
    upper_roof_y_length = pillar_total_height / 3

    draw_background_box(bg_x_length, bg_y_length)
    draw_main_pantheon_walls(bg_y_length, main_building_x_length, main_building_y_length)
    draw_doorway(bg_y_length, door_x_length, door_y_length)
    draw_all_pillars(door_x_length, bg_y_length, pillar_short_x_length, pillar_long_x_length, pillar_y_length,
                     pillar_base_y_length, factor_amount)
    draw_roof(bg_y_length, main_building_x_length, main_building_y_length, upper_roof_x_length, upper_roof_y_length,
              pillar_total_height, factor_amount)


main()

mainloop()

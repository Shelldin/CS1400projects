import turtle
import argparse



def check_value(value):
    try:
        float(value)
    except ValueError as err:
        print(f"{err} please enter a number")


def get_scale_factor():
    parser = argparse.ArgumentParser(description="Get number to scale the turtle drawing")

    parser.add_argument('scale_factor', type=float,
                        help="Enter a number by which the picture will be scaled")

    args = parser.parse_args()

    check_value(args.scale_factor)

    return args.scale_factor



def go_top_left(bg_x_length, bg_y_length):
    """position cursor in top left of picture"""
    turtle.up()
    turtle.goto(bg_x_length / -2, bg_y_length / 2)
    turtle.down()


def go_bottom_left(bg_x_length, bg_y_length):
    """position cursor in bottom left of picture"""
    turtle.up()
    turtle.goto(bg_x_length / -2, bg_y_length / -2)
    turtle.down()


def go_bottom_center(bg_y_length):
    """position cursor in bottom middle of picture"""
    turtle.up()
    turtle.goto(0, bg_y_length / -2)
    turtle.down()


def draw_background_box(bg_x_length, bg_y_length):
    """draw a background/sky box"""
    go_top_left(bg_x_length, bg_y_length)
    turtle.setheading(270)
    turtle.fillcolor("skyblue")
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.fd(bg_y_length)
        else:
            turtle.fd(bg_x_length)
        turtle.lt(90)
    turtle.end_fill()


def draw_doorway(bg_y_length, door_x_length, door_y_length):
    """draw the doorway shape"""
    count = 0
    go_bottom_center(bg_y_length)
    turtle.fillcolor("black")
    turtle.seth(0)
    turtle.up()
    turtle.fd(door_x_length / 2)
    turtle.down()
    turtle.seth(90)
    turtle.begin_fill()

    while count < 4:
        if count % 2 == 0:
            turtle.fd(door_y_length)
        else:
            turtle.fd(door_x_length)
        count += 1
        turtle.lt(90)
    turtle.end_fill()


def draw_pillar_base(pillar_long_x_length, pillar_short_x_length, pillar_base_y_length):
    """draw the base of a pillar"""
    turtle.begin_fill()
    turtle.fd(pillar_long_x_length)
    turtle.goto(turtle.xcor() - (pillar_long_x_length * .25), turtle.ycor() + pillar_base_y_length)
    turtle.goto(turtle.xcor() - pillar_short_x_length, turtle.ycor())
    turtle.goto(turtle.xcor() - (pillar_long_x_length * .25), turtle.ycor() - pillar_base_y_length)
    turtle.end_fill()
    turtle.up()
    turtle.goto(turtle.xcor() + (pillar_long_x_length * .25), turtle.ycor() + pillar_base_y_length)
    turtle.down()


def draw_pillar_column(pillar_y_length, pillar_short_x_length):
    """Draw the main section of the pillar"""
    turtle.seth(90)
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.fd(pillar_y_length)
        else:
            turtle.fd(pillar_short_x_length)
        turtle.rt(90)
    turtle.end_fill()
    turtle.fd(pillar_y_length)


def draw_pillar_top(pillar_short_x_length, pillar_long_x_length, pillar_base_y_length):
    turtle.seth(0)
    turtle.begin_fill()
    turtle.fd(pillar_short_x_length)
    turtle. goto(turtle.xcor() + (pillar_long_x_length * .25), turtle.ycor() + pillar_base_y_length)
    turtle.goto(turtle.xcor() - pillar_long_x_length, turtle.ycor())
    turtle.goto(turtle.xcor() + (pillar_long_x_length * .25), turtle.ycor() - pillar_base_y_length)
    turtle.end_fill()


def draw_all_pillars(door_x_length, bg_y_length, pillar_short_x_length, pillar_long_x_length, pillar_y_length,
                     pillar_base_y_length, factor_amount):
    pillar_count = 8
    turtle.fillcolor("ivory1")
    go_bottom_center(bg_y_length)
    turtle.seth(0)
    turtle.up()
    turtle.fd(door_x_length / 2)

    # draw the right side pillars
    while pillar_count > 4:
        turtle.seth(0)
        turtle.fd(10 * factor_amount)
        turtle.down()
        draw_pillar_base(pillar_long_x_length, pillar_short_x_length, pillar_base_y_length)
        draw_pillar_column(pillar_y_length, pillar_short_x_length)
        draw_pillar_top(pillar_short_x_length, pillar_long_x_length, pillar_base_y_length)
        turtle.up()
        turtle.goto(turtle.xcor() + pillar_short_x_length + (pillar_long_x_length * .25),
                    bg_y_length / -2)
        pillar_count -= 1

    go_bottom_center(bg_y_length)
    turtle.seth(180)
    turtle.up()
    turtle.fd((door_x_length / 2) + (50 * factor_amount) + (pillar_long_x_length * 4))

    # draw left side pillars
    while 0 < pillar_count < 5:
        turtle.seth(0)
        turtle.fd(10 * factor_amount)
        turtle.down()
        draw_pillar_base(pillar_long_x_length, pillar_short_x_length, pillar_base_y_length)
        draw_pillar_column(pillar_y_length, pillar_short_x_length)
        draw_pillar_top(pillar_short_x_length, pillar_long_x_length, pillar_base_y_length)
        turtle.up()
        turtle.goto(turtle.xcor() + pillar_short_x_length + (pillar_long_x_length * .25), bg_y_length / -2)
        pillar_count -= 1


def draw_main_pantheon_walls(bg_y_length, main_building_x_length, main_building_y_length):
    """draw the main building walls of the pantheon"""
    go_bottom_center(bg_y_length)
    turtle.fillcolor("ivory4")
    turtle.up()
    turtle.goto(main_building_x_length / -2, turtle.ycor())
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.fd(main_building_x_length)
        else:
            turtle.fd(main_building_y_length)
        turtle.lt(90)
    turtle.end_fill()


def draw_roof_rectangles(bg_y_length, main_building_x_length, main_building_y_length, factor_amount):
    turtle.fillcolor("ivory1")
    go_bottom_center(bg_y_length)
    turtle.up()
    turtle.goto((main_building_x_length / -2) - (6 * factor_amount), turtle.ycor() + main_building_y_length)
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.fd(main_building_x_length + (12 * factor_amount))
        else:
            turtle.fd(6 * factor_amount)
        turtle.lt(90)
    turtle.end_fill()

    turtle.fillcolor("ivory2")
    turtle.up()
    turtle.goto(turtle.xcor() + (6 * factor_amount), turtle.ycor() + (6 * factor_amount))
    turtle.down()

    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.fd(main_building_x_length)
        else:
            turtle.fd(12 * factor_amount)
        turtle.lt(90)
    turtle.end_fill()

    turtle.fillcolor("ivory1")
    turtle.up()
    turtle.goto(turtle.xcor() - (6 * factor_amount), turtle.ycor() + (12 * factor_amount))
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.fd(main_building_x_length + (12 * factor_amount))
        else:
            turtle.fd(6 * factor_amount)
        turtle.lt(90)
    turtle.end_fill()


def draw_upper_roof(bg_y_length, upper_roof_x_length, upper_roof_y_length, pillar_total_height, factor_amount):
    go_bottom_center(bg_y_length)
    turtle.fillcolor("ivory3")
    turtle.up()
    turtle.goto(turtle.xcor() + (upper_roof_x_length / -2), turtle.ycor() + pillar_total_height + (24 * factor_amount))
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.fd(upper_roof_x_length)
        else:
            turtle.fd(upper_roof_y_length)
        turtle.lt(90)
    turtle.end_fill()

    turtle.fillcolor("ivory2")
    turtle.up()
    turtle.goto((turtle.xcor() - (6 * factor_amount), turtle.ycor() + upper_roof_y_length))
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turtle.fd(upper_roof_x_length + (12 * factor_amount))
        else:
            turtle.fd(6 * factor_amount)
        turtle.lt(90)
    turtle.end_fill()


def draw_roof_triangles(main_building_x_length, factor_amount, t):
    t.fillcolor("ivory1")
    tri_start_pos = t.pos()
    tri_side_count = 0
    t.seth(0)
    t.down()
    t.begin_fill()
    while tri_side_count < 3:
        if tri_side_count == 0:
            t.goto(0, t.ycor() + (48 * factor_amount))
            tri_side_count += 1
        elif tri_side_count == 1:
            t.goto(tri_start_pos)
            t.seth(0)
            t.fd(main_building_x_length + (12 * factor_amount))
            tri_side_count += 1
        elif tri_side_count == 2:
            t.goto(0, t.ycor() + (48 * factor_amount))
            tri_side_count += 1
        else:
            break
    t.end_fill()

    t.fillcolor("ivory2")
    t.up()
    t.goto(tri_start_pos)
    t.goto(t.xcor() + (28 * factor_amount), t.ycor())
    second_tri_start_pos = t.pos()
    tri_side_count = 0
    t.down()
    t.begin_fill()
    while tri_side_count < 3:
        if tri_side_count == 0:
            t.goto(0, t.ycor() + (40 * factor_amount))
            tri_side_count += 1
        elif tri_side_count == 1:
            t.goto(second_tri_start_pos)
            t.seth(0)
            t.fd(main_building_x_length - (48 * factor_amount))
            tri_side_count += 1
        elif tri_side_count == 2:
            t.goto(0, t.ycor() + (40 * factor_amount))
            tri_side_count += 1
        else:
            break
    t.end_fill()


def draw_dome(dome_radius, upper_roof_y_length, factor_amount, t):
    t.fillcolor("ivory2")
    t.up()
    t.goto(0, t.ycor() + upper_roof_y_length + (12 * factor_amount))
    t.goto(t.xcor() - dome_radius, t.ycor())
    t.down()
    t.seth(90)
    t.begin_fill()
    t.circle(-dome_radius, 180)
    t.end_fill()


def draw_roof(bg_y_length, main_building_x_length, main_building_y_length, upper_roof_x_length, upper_roof_y_length,
              pillar_total_height, dome_radius, factor_amount, t):
    draw_roof_rectangles(bg_y_length, main_building_x_length, main_building_y_length, factor_amount)
    roof_left_edge = t.pos()
    draw_upper_roof(bg_y_length, upper_roof_x_length, upper_roof_y_length, pillar_total_height, factor_amount)
    t.up()
    t.goto(roof_left_edge)
    t.goto(t.xcor(), t.ycor() + (6 * factor_amount))
    draw_roof_triangles(main_building_x_length, factor_amount)
    t.up()
    t.goto(roof_left_edge)
    draw_dome(dome_radius, upper_roof_y_length, factor_amount)


def main():
    # size factor
    factor_amount = get_scale_factor()

    # background dimension variables
    bg_x_length = 560 * factor_amount
    bg_y_length = 340 * factor_amount

    # door dimension variables
    door_x_length = 60 * factor_amount
    door_y_length = 100 * factor_amount

    # variables for the pillar functions
    pillar_long_x_length = 40 * factor_amount
    pillar_short_x_length = 20 * factor_amount
    pillar_y_length = 120 * factor_amount
    pillar_base_y_length = pillar_long_x_length / 2
    pillar_total_height = pillar_y_length + pillar_base_y_length * 2

    # base building variables
    main_building_x_length = door_x_length + (80 * factor_amount) + (pillar_long_x_length * 8)
    main_building_y_length = pillar_total_height

    # upper roof dimension variables
    upper_roof_x_length = door_x_length + (60 * factor_amount) + (pillar_long_x_length * 8)
    upper_roof_y_length = pillar_total_height / 3

    # dome
    dome_radius = 88 * factor_amount

    draw_background_box(bg_x_length, bg_y_length)
    draw_main_pantheon_walls(bg_y_length, main_building_x_length, main_building_y_length)
    draw_doorway(bg_y_length, door_x_length, door_y_length)
    draw_all_pillars(door_x_length, bg_y_length, pillar_short_x_length, pillar_long_x_length, pillar_y_length,
                     pillar_base_y_length, factor_amount)
    draw_roof(bg_y_length, main_building_x_length, main_building_y_length, upper_roof_x_length, upper_roof_y_length,
              pillar_total_height, dome_radius, factor_amount)


if __name__ == "__main__":
    main()
    turtle.done()
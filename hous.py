import math
import turtle as t
t.speed (0)
t.shape ("turtle")


def draw_hous(walls_x, walls_y, walls_width, walls_height, walls_colors, door_width, door_height, door_colors, roof_height , roof_colors):
	door_x = walls_x + walls_width / 2 - door_width / 2

	door_y = walls_y

	roof_x = walls_x

	roof_y = walls_y + walls_height

	roof_side = math.sqrt(roof_height ** 2 + (walls_width / 2) ** 2)
	roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))

	draw_walls(walls_x, walls_y, walls_width, walls_height, walls_colors)
	draw_door(door_x, door_y, door_width, door_height, door_colors)
	draw_roof(roof_x, roof_y, roof_side ,roof_angle ,roof_colors )


def draw_walls(walls_x, walls_y, walls_width, walls_height, walls_colors):
	t.setheading(0)
	t.penup()
	t.goto(walls_x, walls_y)
	t.pendown()
	t.fillcolor(walls_colors)
	t.begin_fill()
	for i in range(2):
		t.fd(walls_width)
		t.left(90)
		t.fd(walls_height)
		t.left(90)
	t.end_fill()


def draw_door(door_x, door_y, door_width, door_height, door_colors):
	t.penup()
	t.goto(door_x, door_y,)
	t.pendown()
	t.fillcolor(door_colors)
	t.begin_fill()
	for i in range(2):
		t.fd(door_width)
		t.left(90)
		t.fd(door_height)
		t.left(90)
	t.end_fill()


def draw_roof(roof_x, roof_y, roof_side ,roof_angle ,roof_colors ):
	t.penup()
	t.goto(roof_x, roof_y)
	t.pendown()
	t.fillcolor(roof_colors)
	t.begin_fill()
	t.left(roof_angle)
	t.fd(roof_side)
	t.right(roof_angle * 2)
	t.fd(roof_side)
	t.end_fill()



draw_hous(100, 50, 100, 105, "#fffff0", 25, 50 ,"red", 45, "#ff0ff0")
draw_hous(-300, -50, 150, 200, "#0000ff", 25, 50 ,"black",100, "#0ffff0")
t.done()
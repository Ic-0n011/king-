import math
import turtle as t
t.speed ()
t.shape ("turtle")


def draw_hous(walls_x, walls_y, walls_width, walls_height, walls_colors,):
	
	draw_walls(walls_x, walls_y, walls_width, walls_height, walls_colors)
	draw_door(door_x, door_y, door_width, door_height, door_colors)
	draw_roof()


def draw_walls(walls_x, walls_y, walls_width, walls_height, walls_colors):
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


def draw_roof():
	print(1)



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



draw_hous(23, 44, 300, 200, "#ff00ff")

t.done()
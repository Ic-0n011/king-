import turtle as t 
import random
t.shape("turtle")
t.speed(-0)
t.colormode(255)
while True:
	x = random.randint(-300, 300)
	y = random.randint(-300, 300)
	circle = random.randint(1, 100)
	radius = random.randint(20, 50)
	red = random.randint(0, 255)
	blue = random.randint(0, 255)
	grean = random.randint(0, 255)

	t.penup()
	t.goto(x, y)
	t.pendown()

	for i in range(circle):
		t.fillcolor(red, blue, grean)
		t.begin_fill()
		t.pendown()
		t.circle(radius)
		t.end_fill()
		t.penup()
		t.setheading(90)
		t.fd(radius * 2)
		t.setheading(0)
		radius /= 1.3
		if radius < 2:
			break

























# контракт
# место снеговика
# радиус первого круга
# следующий круг в два раза меньше предыдущего
# колличество кругов
# цвут кругов


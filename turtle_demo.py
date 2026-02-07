import turtle as t


def draw_star(size, x=0, y=0, color="gold"):
	t.penup()
	t.goto(x, y)
	t.pendown()
	t.color(color)
	t.begin_fill() 
	for _ in range(5):
		t.forward(size)
		t.right(144)
	t.end_fill()


def main():
	screen = t.Screen()
	screen.bgcolor("midnight blue")
	t.speed(3)
	t.pensize(2)

	# draw a few stars of different sizes/positions
	draw_star(120, 0, -20, "gold")
	draw_star(60, -160, 80, "lightyellow")
	draw_star(40, 140, 100, "white")
	draw_star(30, -60, 160, "lightblue")

	t.hideturtle()

	# Wait for user click to close the window
	t.exitonclick()


if __name__ == "__main__":
	main()

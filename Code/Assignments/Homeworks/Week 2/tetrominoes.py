from graphics import *

class Block(Rectangle):
	def __init__(self, point, color):
		Rectangle.__init__(self, Point(point.x*30, point.y*30), Point(point.x*30 + 30, point.y*30 + 30))
		self.setFill(color)
		self.setWidth(3)

class Shape:
	def __init__(self, coords, color):
		self.coords = coords
		self.color = color
	def draw(self, win):
		for coord in self.coords:
			Block(coord, self.color).draw(win)

class I_Shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 2, center.y),
				  Point(center.x - 1, center.y),
				  Point(center.x, center.y),
				  Point(center.x + 1, center.y)]

		Shape.__init__(self, coords, "blue")

class J_Shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x, center.y),
				  Point(center.x + 1, center.y),
				  Point(center.x + 1, center.y + 1)]

		Shape.__init__(self, coords, "orange")

class L_Shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y + 1),
				  Point(center.x - 1, center.y),
				  Point(center.x, center.y),
				  Point(center.x + 1, center.y)]

		Shape.__init__(self, coords, "sky blue")

class O_Shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x - 1, center.y + 1),
				  Point(center.x, center.y),
				  Point(center.x, center.y + 1)]

		Shape.__init__(self, coords, "red")

class S_Shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y + 1),
				  Point(center.x, center.y + 1),
				  Point(center.x, center.y),
				  Point(center.x + 1, center.y)]

		Shape.__init__(self, coords, "green")
class T_Shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x, center.y + 1),
				  Point(center.x, center.y),
				  Point(center.x + 1, center.y)]

		Shape.__init__(self, coords, "yellow")

class Z_Shape(Shape):
	def __init__(self, center):
		coords = [Point(center.x - 1, center.y),
				  Point(center.x, center.y),
				  Point(center.x, center.y + 1),
				  Point(center.x + 1, center.y + 1)]

		Shape.__init__(self, coords, "purple")

win = GraphWin("Tetrominoes", 900, 150)

tetrominoes = [I_Shape, J_Shape, L_Shape, O_Shape, S_Shape, T_Shape, Z_Shape]
x = 3

for tetromino in tetrominoes:
	shape = tetromino(Point(x, 1))
	shape.draw(win)
	x += 4

win.mainloop()

shape = I_Shape(Point(3, 1))
shape.draw(win)

win.mainloop()
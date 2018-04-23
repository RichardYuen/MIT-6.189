from graphics import *
from wheel import *

class Car():
	def __init__(self, center1, radius1, center2, radius2, height):
		self.wheel1 = Wheel(center1, radius1, 0.6*radius1)
		self.wheel2 = Wheel(center2, radius2, 0.6*radius2)
		self.body = Rectangle(Point(center1.x, center1.y - height), Point(center2.x, center2.y))

	def draw(self, win):
		self.body.draw(win)
		self.wheel1.draw(win)
		self.wheel2.draw(win)

	def set_color(self, tire_color, wheel_color, body_color):
		self.wheel1.set_color(wheel_color, tire_color)
		self.wheel2.set_color(wheel_color, tire_color)
		self.body.setFill(body_color)

	def animate(self, win, dx, dy, n):
		if n > 0:
			self.body.move(dx, dy)
			self.wheel1.move(dx, dy)
			self.wheel2.move(dx, dy)
			win.after(100, self.animate, win, dx, dy, n-1)

new_win = GraphWin('A Car', 700, 300)
car1 = Car(Point(50, 50), 15, Point(100, 50), 15, 40)
car1.draw(new_win)
car1.set_color('blue', 'green', 'red')

car1.animate(new_win, 1, 0, 400)

new_win.mainloop()
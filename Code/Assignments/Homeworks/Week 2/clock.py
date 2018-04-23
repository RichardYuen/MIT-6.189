from graphics import *
import math

class Clock:
	def __init__(self, win, hour, minute, second):
		self.hour = hour
		self.minute = minute
		self.second = second
		self.center = Point((win.width - 1) / 2, (win.height - 1)/ 2)
	
class DigitalClock(Clock):
	def tick(self, win, n = 1):
		if n > 0:
			self.update()
			win.after(1000, self.tick, win, n+1)
	
	def Status(self):
		if self.hour > 12:
			state = 'PM'
			hour = self.hour % 12
		else:
			state = 'AM'
			if self.hour == 0:
				hour = 12
			else:
				hour = self.hour
		return "%02d:%02d:%02d %s" % (hour, self.minute, self.second, state)	


	def update(self):
		seconds = self.second + self.minute*60 + self.hour*3600
		seconds += 1
		
		self.second = (seconds % 3600) % 60
		self.minute = (seconds // 60) % 60
		self.hour = (seconds // 3600)

		self.display.setText(self.Status())	

	def draw_face(self, win, color = "dark green"):
		face = Rectangle(Point(10, 10), Point(win.width - 11, win.height - 11))
		face.setFill(color)
		face.setWidth(5)
		face.draw(win)

	def draw_text(self, win):
		self.display = Text(self.center, self.Status())
		self.display.setSize(int((7.0 / 60.0) * win.width))
		self.display.draw(win)

	def draw(self, win):
		self.draw_face(win)
		self.draw_text(win)

class ClockHand(Line):
	"""Class Object for Clock Hand as a Line"""
	def __init__(self, clock, hand_len, type):
		if type == 'hour':
			self.alpha = (clock.hour % 12 + clock.minute / 60.0 + clock.second / 3600.0) * (math.pi / 6)
		elif type == 'minute':
			self.alpha  = (clock.minute + clock.second / 60.0) * (math.pi / 30)
		elif type == 'second':
			self.alpha  = (clock.second) * (math.pi / 30)  
		
		self.hand_len = hand_len
		self.p1 = clock.center
		self.p2 = Point(clock.center.x + math.sin(self.alpha)* self.hand_len,\
		clock.center.y - math.cos(self.alpha)*self.hand_len)

		Line.__init__(self, self.p1, self.p2)
		
class AnalogClock(Clock):
	def __init__(self, win, hour, minute, second, radius):
		Clock.__init__(self, win, hour, minute, second)
		self.center = Point((win.width - 1) / 2, (win.height - 1) / 2)
		self.radius = radius

	def draw(self, win):
		self.draw_face(win)
		self.draw_digits(win)
		self.center.draw(win)
		self.draw_hour_hand(win)
		self.draw_minute_hand(win)
		self.draw_second_hand(win)
	
	def tick(self, win, n = 1):
		if n > 0:
			self.update(win)
			win.after(1000, self.tick, win, n+1)

	def update(self, win):
		self.second_hand.undraw()
		self.minute_hand.undraw()
		self.hour_hand.undraw()

		seconds = self.second + self.minute*60 + self.hour*3600
		seconds += 1
		
		self.hour = seconds // 3600
		self.minute = (seconds % 3600) // 60
		self.second = (seconds % 3600) % 60

		self.draw_hour_hand(win)
		self.draw_minute_hand(win)
		self.draw_second_hand(win)

	def draw_face(self, win, color = 'violet'):
		face = Circle(self.center, self.radius)
		face.setFill(color)
		face.setWidth(3)
		face.draw(win)

	def draw_digits(self, win):
		l = self.radius * 0.9
		for dig in range(12):
			dy = - l * math.cos(math.pi/6 * dig)
			dx = l * math.sin(math.pi/6 * dig)
			if dig == 0: dig = '12'
			else: dig = str(dig)
			digit = Text(Point(self.center.x + dx, self.center.y + dy), dig)
			digit.setSize(10)
			digit.draw(win)

	def draw_hour_hand(self, win, color = 'black'):
		length = self.radius * 0.5
		self.hour_hand = ClockHand(clock, length, 'hour')
		self.hour_hand.setFill(color)
		self.hour_hand.setWidth(5)
		self.hour_hand.draw(win)

	def draw_minute_hand(self, win, color = 'black'):
		length = self.radius * 0.7
		self.minute_hand = ClockHand(clock, length, 'minute')
		self.minute_hand.setFill(color)
		self.minute_hand.setWidth(5)
		self.minute_hand.draw(win)

	def draw_second_hand(self, win, color = 'black'):
		length = self.radius * 0.7
		self.second_hand = ClockHand(clock, length, 'second')
		self.second_hand.setFill(color)
		self.second_hand.setWidth(3)
		self.second_hand.draw(win)


# create the graphics window
new_win = GraphWin("Analog Clock", 300, 300)
clock = AnalogClock(new_win, 8, 30, 05, 100)
clock.draw(new_win)
clock.tick(new_win)
new_win.mainloop()
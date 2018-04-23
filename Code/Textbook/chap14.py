#####Section 14.3
class Time:
	def convertToSeconds(self):
		minutes = self.hours * 60 + self.minutes 
		seconds = minutes * 60 + self.seconds

		return seconds

currentTime = Time()
currentTime.hours = 20
currentTime.minutes = 59
currentTime.seconds = 13
print currentTime.convertToSeconds()
#####Section 14.5
def find(str, ch, start=0, end = None):
	if end == None: end = len(str) 
  	index = start
  	while index < end: 
  		if str[index] == ch: 
  			return index 

  		index = index + 1 
  	return -1

print find("apple", "a", end = 2) #Return 0
print find("apple", "e", end = 2) #Return -1
print find("fuckyou", "y", 2) #Return 4
#####Section 14.8
class Point: 
	def __init__(self, x=0, y=0): 
		self.x = x 
		self.y = y 

	def __str__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')' 

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return Point(self.x * other,x, self.y * other.y)

	def __rmul__(self, other):
		return Point(self.x * other, self.y * other)

	def reverse(self):
		self.x , self. y = self.y , self. x

p1 = Point(3, 4)
p2 = Point(5, 7)
p3 = p1 + p2
p4 = p1 - p2
print p3
print p4



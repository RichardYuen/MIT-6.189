class Point::
	pass
class Rectangle:
	pass
def distance(p1, p2):
	dx = p2.x - p1.x
	dy = p2.y - p1.y
	dsquared = dx**2 + dy**2
	result = math.sqrt(dsquared)
	return result

def moveRect(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy

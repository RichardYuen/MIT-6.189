class Stack:
	def __init__(self):
		self.elements = []
	def push(self, X):
		self.elements.insert(0, X)
	def pop(self):
		if len(self.elements) == 0:
			return "The stack is empty"
		else:
			return self.elements.pop(0)

stack = Stack()
stack.push(5)
stack.push(6)
print stack.pop()
stack.push(7)
print stack.pop()
print stack.pop()
print stack.pop()		
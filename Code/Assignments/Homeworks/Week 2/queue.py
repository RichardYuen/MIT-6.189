class Queue:
	def __init__(self):
		self.elements = []
	def insert(self, X):
		self.elements.append(X)
	def remove(self): 
		if len(self.queue) == 0:
			return "The queue is empty"
		else:
			return self.queue.pop(0)

class Queue_by_nodes:
	class Node(self):
		def __init__:
			self.Element = None
			self.Next = None	
	def __init__(self, Node):
		self.Node = Node
	def insert(self,ss X):
		New = Node()
		self.Node.Element = X
		self.Node.Next = New
	def remove(self):
		self.Node		

queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
queue.insert(7)
queue.remove()
queue.remove()
queue.remove()
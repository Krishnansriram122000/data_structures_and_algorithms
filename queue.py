from linkedlist import node
class queue:
	def __init__(self):
		self._front=None
		self._rear=None
	def enqueue(self,data):
		if self._front==self._rear==None :
			self._front=self._rear=node(data)
			return
		self._rear.next=node(data)
		self._rear=self._rear.next
	def dequeue(self):
		s=self._front.data
		n=self._front
		self._front=self._front.next
		if self._front==None:
			self._rear=None
		del n
		return s

r=queue()
r.enqueue(45)
r.enqueue(21)
r.enqueue(90)
for _ in range(3):
	print(r.dequeue())

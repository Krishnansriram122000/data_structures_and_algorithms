from linkedlist import node 
class stack:
	def __init__(self):
		self._top=None
	def push(self,data):
		n=node(data)
		n.next=self._top
		self._top=n
	def pop(self):
		if self._top==None:
			print('empty')
		else:
			n=self._top
			self._top=n.next
			s=n.data
			del n
			return s
	def peek(self):
		print(self._top.data)
			
s=stack()
s.push(34)
s.push(45)
s.push(35)
s.push(23)
print(s.pop())
s.peek()
class node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None
class list1:
	def __init__(self):
		self._head=None
	def inbeg(self,data):
		n=node(data)
		n.next=self._head
		self._head=n
	def dis(self):
		#n=node()
		n=self._head
		while(n!=None):
			print (n.data)
			n=n.next
	def inend(self,data):
		n=self._head
		if n!=None:
			while(n.next!=None):
				n=n.next
			n.next=node(data)
		else :
			self._head=node(data)

if __name__=='__main__' :
	l=list1()
	for _ in range(5):
		a=int(input('enter'))
		l.inend(a)
	l.dis()



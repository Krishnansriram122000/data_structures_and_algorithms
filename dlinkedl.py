from linkedlist import node,list1
class dl(list1):
	def inbeg(self,data):
		n=node(data)
		n.next=self._head
		self._head=n
		if n.next!=None:
			n.next.prev=n
	def inend(self,data):
		n=self._head
		if n!=None:
			while(n.next!=None):
				n=n.next
			n.next=node(data)
			n.next.prev=n
		else :
			self._head=node(data)
	def rev(self):
		n=self._head
		while(n.next!=None):
			n=n.next
		while(n!=None):
			print(n.data)
			n=n.prev
if __name__=='__main__':
	y=dl()
	y.inend(34)
	y.inend(45)
	y.inend(342)
	y.inend(23)
	y.dis()
	y.dis()
	print('reverse')
	y.rev()

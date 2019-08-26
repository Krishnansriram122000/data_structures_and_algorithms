from dlinkedl import dl,node
class cir(dl):
	def inend(self,data):
		n=self._head
		if n!=None:
			while(n.next!=self._head):
				n=n.next
			n.next=node(data)
			n.next.prev=n
			n.next.next=self._head
			self._head.prev=n.next
		else :
			self._head=node(data)
			self._head.next=self._head
	def dis(self):
		#n=node()
		n=self._head
		while(True):
			print (n.data)
			n=n.next
			if n==self._head or n==None:
				break
	def inbeg(self,data):
		n=node(data)
		n.next=self._head
		n.prev=self._head.prev
		self._head=n
		n.next.prev=n
		n.prev.next=n

o=cir()
o.inend(34)
o.dis()
o.inend(98)
o.dis()
o.inend(25)
o.dis()
o.inbeg(56)
o.dis()
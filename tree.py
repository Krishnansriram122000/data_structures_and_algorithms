class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		
		
class tree:
	def __init__(self):
		self.root=None
		self.ins
	def insert(self,data):
		if self.root==None:
			self.root=node(data)
			return
		n=self.root
		self.ins(n,data)
	def ins(self,n,data):
		if data<n.data:
			if n.left==None:
				n.left=node(data)
				return
			n=n.left
			self.ins(n,data)
		else :
			if n.right==None:
				n.right=node(data)
				return
			n=n.right
			self.ins(n,data)
t=tree()
t.insert(90)
t.insert(34)
t.insert(8)
t.insert(24)
t.insert(32)
t.insert(23)
t.insert(102)
t.insert(65)
t.insert(21)
t.insert(80)
		

class Node:Node
	
	def __init__(self, value):
		self.data = value
		self.next = None


class Stack:

	def __init__(self):
		self.top = None

	def isempty(self):
		return self.top == None

	def push(self, value):

		new_node = Node(value)

		new_node.next = self.top

		self.top = new_node

	def peek(self):
		if self.isempty():
			return 'Stack Empty'
		else:
			return self.top.data

	def pop(self):
		if self.isempty():
			return 'Stack Empty'
		else:
			self.top = self.top.next

	def traverse(self):

		temp = self.top

		while temp != None:

			print(temp.data)
			temp = temp.next



s = Stack()

s.isempty()
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.isempty()


def find_the_celeb(L):

	s = Stack()

	for i in traverse(len(L)):
		s.push (i)


	while s.size() >= 2:
		i = s.pop()
		j = s.pop()

		# j is not celeb
		if L[i][j] == 0:
			s.push(i)
		# i is not celeb	
		else:
			s.push(j)

	celeb = s.pop()

	for i in range(len(L)):
		if i != celeb:
			if L[i][celeb] == 0 or L[celeb][i] == 1:
				print("No one is celebrity")
				return

	print('The celebrity is ', celeb)


L = [
	[0, 0, 1, 1],
	[0, 0, 1, 0],
	[0, 0, 0, 0],
	[0, 0, 1, 0]
]

find_the_celeb(L)



l = '[{ (a+b) + (c+d)}]'


def check_parenthesis(l):

	s = Stack() 
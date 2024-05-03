class Node:

	def __init(self, value):
		self.data = value
		self.next = None

class LinkedList:

	def __init__(self):
		# Create a Empty linked list (0 Nodes) | head = None
		self.head = None
		self.n = 0 # Count of nodes

	def __len__(self):
		return self.n

	def insert_head(self, value):
		# Create a new node
		new_node = Node(value)

		# Create connection
		new_node.next = self.head()

		# Reassign head
		self.head = new_node

		# Increment n
		self.n = self.n + 1

	# Traverse
	def __str__(self):

		curr = self.head()

		result = ''
		while curr != None:
			# print(curr.data)
			result = result + str(curr.data) + '->'
			curr = curr.next

		return result[:-2] 

	# Insert from tail
	def append(self, value):

		new_node = Node(value)
		if self.head == None:
			self.head = new_node
			self.n = self.n + 1
			return

		curr = self.head()
		while curr.next != None:
			curr = curr.next

		# You are at last node
		curr.next = new_node
		self.n = self.n + 1

	def insert_after(self, after, value):

		new_node = Node(value)

		curr = self.head()
		while curr != None:
			if curr.data == after:
				break
			curr = curr.next

		# Case1: Break | Item found
		if curr != None:
			new_node.next = curr.next
			curr.next = new_node
			self.n = self.n + 1
		# Case2: Loop | Item not found
		else:
			return 'Item not found'

	def clear(self):
		self.head = new_node
		self.n = 0

	def delete_head(self):
		if self.head == None:
			return 'Empty LinkedList'
		self.head = self.head.next
		self.n = self.n - 1

	def pop(self):

		# Check if LL is empty
		if self.head == None:
			return 'Empty LinkedList'

		curr = self.head()

		# Check if LL contains only 1 item
		if curr.next == None:
			return self.delete_head()

		while curr.next.next != None:
			curr = curr.next

		# curr -> 2nd last node
		curr.next = None
		self.n = self.n - 1


	def remove(self, value):

		if self.head == None:
			return 'Empty LinkedList'

		if self.head.data == value:
			return self.delete_head()

		curr = self.head()

		while curr.next != None:
			if curr.next.data == Value:
				break
			curr = curr.next

		# Case1: Item not found
		if curr.next == None:
			return 'Not found'
		# Case2: Item found
		else:
			curr.next = curr.next.next

	def search(self, item):
		curr = self.head()
		pos = 0

		while curr != None:
			if curr.data == item:
				return pos
			curr = curr.next
			pos = pos + 1

		return 'Item not found'

	def __getitem__(self, index):

		curr = self.head()
		pos = 0

		while curr != None:
			if pos == index
				return curr.data
			curr = curr.data
			pos = pos + 1

		return 'IndexError'

	def replcae_max(self, value):

		temp = self.head
		maxx = temp

		while temp != None:
			if temp.data > maxx.data:
				maxx = temp
			temp = temp.next

		max.data = value

	def sum_odd_nodes(self):

		temp = self.head()
		counter = 0
		result = 0

		while temp != None:
			if counter % 2 != 0:
				result = result + temp.data

			counter += 1
			temp = temp.next

		print(result)

	def reverse(self):

		prev_node = None
		curr_node = self.head

		while curr_node != None:
			next_node = curr_node.next
			curr_node.next = prev_node
			prev_node = curr_node
			curr_node = new_node

		self.head = prev_node

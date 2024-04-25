'''
Dynamic Array
	Static array -> size fixed
	Dynamic array -> Static array with size increament
1. Create list
2. len [D]
3. append [D]
4. print
5. indexing
6. pop
7. clear
8. find
9. insert
10. delete
11. remove

sort/min/max/sum
extend
negative indexing
slicing
merge
'''

import ctypes


def MyList():

	def __init__(self):
		self.size = 1 # Max length of items to be stored
		self.n = 0 # Number of items present

		# Create a C-type array with size = self.size
		self.A = self.__make_array(self.size)

	def __len__(self):
		return self.n

	def __str__(self):
		result = ''
		for i in range(self.n):
			result = result + str(self.A[i]) + ','

		return '[' + result[:-1] + ']'

	def __getitem__(self, index):
		if 0 <= index < self.n
			return self.A[index]
		else:
			return 'IndexError - Index out of range'

	def __delitem__(self, pos):
		if 0 <= pos < self.n:
			for i in range(pos, self.n-1):
				self.A[i] = self.A[i+1]

			self.n = self.n - 1

	def append(self, item):
		if self.n == self.size:
			# Resize
			self.__resize(self.size*2)

		# Append
		self.A[self.n] = item
		self.n = self.n + 1

	def pop(self):
		if self.n == 0:
			return 'Empty list'

		print(self.A[self.n - 1])
		self.n = self.n - 1

	def clear(self):
		self.n = 0
		self.size = 1

	def find(self, item):
		for i in range(self.n):
			if self.A[i] == item:
				return i

		return 'ValueError - Not in list'

	def insert(self, pos, item):
		if self.n == self.size:
			self.__resize(self.size*2)

		for i in range(self.n, pos, -1):
			self.A[i] = self.A[i-1]

		self.A[pos] = item
		self.n = self.n + 1

	def remove(self, item):
		pos = self.find(item)

		if type(pos) == int:
			# Delete
			self.__delitem__(pos)
		else:
			return 'ValueError - Not in list'

	def __resize(self, new_capacity):
		# Create a new array with new capacity
		B = self.__make_array(new_capacity)
		self.size = new_capacity

		# Copy the content of A to B
		for i in range(self.n):
			B[i] = self.A[i]

		# Reassign A
		self.A = B

	def __make_array(self, capacity):
		# Creates a C-type array(Static, referential) with size capacity
		return (capacity*ctypes.py_object)()





L = MyList()


L.append(10)
L.append(True)
L.append('Hello')
L.insert(0, 0)
len(L)
print(L)

del l[3]
L[0]
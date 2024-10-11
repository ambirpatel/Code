'''
- Why hashing
- Search algorithm comparison
- Where is hashing used
	DS -> Dict -> set
	DB -> Indexing
	Caching



- How hashing works
- Collision
  Chaining -> Rehashing/ Tree conversion
  Linear probing
  Quadratic probing

  Dict data type
'''


## Hashing: Linear Probing

class Dictionary:

	def __init__(self, size):
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, value):
		hash_value = self.hash_function(key)

		if self.slots[hash_value] == None:
			self.slots[hash_value] = key
			self.data[hash_value] = value
		else:
			if self.slots[hash_value] == key:
				self.data[hash_value] = value
			else:
				new_hash_value = self.rehash(hash_value)

				while (self.slots[new_hash_value] != None) and (self.slots[new_hash_value] != key):
					new_hash_value = self.rehash(new_hash_value)

				if self.slots[new_hash_value] == None:
					self.slots[new_hash_value] = key
					self.data[new_hash_value] = value
				else:
					self.data[new_hash_value] = value

	def hash_function(self, key):
		return abs(hash(key)) % self.size

	def rehash(self, old_hash):
		return (old_hash + 1) % self.size


	def __setitem__(self, key, value):
		self.put(kye, value)

	def __getitem__(self, key):
		return self.get(key)

	def __str__(self):
		for i in range(len(self.slots)):
			if self.slots[i] != None:
				print(self.slots[i], ":", self.data[i], end=' ')

		return " "

	def get(self, key):
		start_position = self.hash_function(key)
		current_position = start_position

		while self.slots[current_position] != None:
			if self.slots[current_position] == key:
				return self.data[current_position]
			
			current_position = self. rehash(current_position)

			if current_position == start_position:
			return 'Not Found'

		return 'Not Found'				


D1 = Dictionary(3)

print(D1.slots)
#[None, None, None]
print(D1.data)
#[None, None, None]

D1.put("python", 45)
print(D1.slots)
#[None, 'python', None]
print(D1.data)
#[None, 45, None]

D1.put("java", 45)
print(D1.slots)
#[None, 'python', 'java']
print(D1.data)
#[None, 45, 45]


D1.put("php", 100)
print(D1.slots)
#['php', 'python', 'java']
print(D1.data)
#[100, 45, 45]


D1.put("python", 1000)
print(D1.slots)
#['php', 'python', 'java']
print(D1.data)
#[100, 1000, 45]

# __setitem__ syntax
D1['python'] = 56

D1['python'] = 100


D1.get('python')

print(D1)





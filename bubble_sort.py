'''
# Why called bubble sort
	After sucessive passes the largest items moves to right.

# Viz: 
	https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/

# Time Complexity
	Number of passes: n - 1
	Number of comparisons:  1+2+3+.....+(n-1)
							n(n+1)/2
							n^2
	O(n^2) | Quadratic

# Space complexity
	O(1) | Constant, since we are not creating any new variables
	
# Adaptive sort?
	A sorting alg falls into the adaptive sort familty if it takes advantage of existing order in its input.
	
	Bubble sort is not adaptive.

	We can make this adaptive by checking swap count.

# Stable?
	If two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.
	
	Bubble sort is stable.



'''

# Regular # Time Complexity o(n*n) | worst case 
def bubble_sort(arr):  

	for i in range(len(arr) - 1):
		for j in range(len(arr) - 1 - i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

	print(arr)


arr = [23, 12, 34, 11, 100, 56, 78]
bubble_sort(arr)


# Adaptive # Time Complexity o(n) | if sorted array | best case
def bubble_sort(arr):

	for i in range(len(arr) - 1):
		flag = 0
		for j in range(len(arr) - 1 - i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				flag = 1

		if flag == 0:
			break
	print(arr)


arr = [23, 12, 34, 11, 100, 56, 78]
bubble_sort(arr)


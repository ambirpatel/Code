# Linear Searching: Brute force | go through each item and match

# Binary search: List needs to be sorted 

# Sleep Sort
# Monkey Sort
# Bubble Sort
# Selection
# Merge sort
# Quick sort


# Insertion sort


# Linear Search 
# Brute force
# Time complexity o(n)

def linear_search(arr, item):
	for i in range(len(arr)):
		if arr[i] == item:
			return i
	return -1 


# Binary sreach
# Sorted array
# Time complexity nlog(n) + log(n) (Ammortize cost)

def binary_search(arr, low, high, item):
	print("low= ", low, "high= ", high, end=" ")
	if low <= high:
		mid = (low + hig) // 2
		print("mid value is ", arr[mid])
		if arr[mid] == item:
			return mid
		elif arr[mid] > item:
			return binary_search(arr, low, mid-1, item)
		else:
			return binary_search(arr, mid+1, high, item)
	else:
		return -1 # Not found


arr = [12, 24, 35, 56, 67, 88, 99]
print(binary_search(arr, 0, len(arr)-1, 88))



# Sorting

def is_sorted(arr):
	sorted = True

	for i in range(len(arr)-1):
		if arr[i] > arr[i+1]
			sorted = False:

	return sorted


arr =[1,2,3,4,5,6]
is_sorted(arr)


# Monkey sort
# Time complexity infinite

import random

def monkey_sort(arr):

	while not is_sorted(arr):
		random.shuffle(arr)
		print(arr)

	print(arr)


# Sleep sort
# print the item after how much value it represents




# Selection sort
# Not adaptive
# Not stable
# time o(n^2)
# space o(1)
# Benifits: Swappings are less 

def selection_sort(arr):

	for i in range(len(arr) - 1):

		print(i+1, "pass", end=" ")
		
		min = i

		print("current min is", arr[min])

		for j in range(i+1, len(arr)):
			print("current item under observation ", arr[j])
			if arr[j] < arr[min]:
				print("Current item is less than min")
				min = j
				print("Now the min has become ", arr[min])

		arr[i], arr[min] = arr[min], arr[i]
		print("*"*50)

	# print(arr)
	return arr





















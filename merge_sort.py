'''
# Why called merge sort
	Works on technique called divide and conquer.

# Viz: 
	https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/visualize/

# Time Complexity
	O(nlog(n))

	divide log(n)
	merge/conquer n

# Space complexity
	creating new array since using recursion
	O(n)

# Adaptive sort?
	A sorting alg falls into the adaptive sort familty if it takes advantage of existing order in its input.
	
	Not adaptive
	
# Stable?
	If two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.
	
'''

# Space complexity o(2n)
def merge_sorted(arr1, arr2):

	i = j = 0
	merged =[]

	while (i < len(arr1)) and (j < len(arr2)):

		if arr1[i] < arr2[j]:
			merged.append(arr1[i])
			i += 1
		else:
			merged.append(arr2[j])
			j += 1

	while i < len(arr1):
		merged.appned(arr1[i])
		i += 1

	while j < len(arr2):
		merged.append(arr2[j])
		j += 1

	return merged


arr1 = [1, 2, 4]
arr2 = [3, 5, 7, 8, 9]

merge_sorted(arr1, arr2)

def merge_sort(arr):

	if len(arr) == 1:
		return arr

	mid = len(arr) // 2

	left = arr[:mid] #left array
	right = arr[mid:] #right array

	left = merge_sort(left)
	right = merge_sort(right)

	return merge_sorted(left, right)

arr = [2, 1, 5, 8, 9, 6, 7, 4]
merge_sort(arr)








# Space complexity o(n)
def merge_sorted(arr1, arr2, arr):

	i = j = k = 0

	while (i < len(arr1)) and (j < len(arr2)):

		if arr1[i] < arr2[j]:
			arr[k] = arr1[i]
			i += 1
		else:
			arr[k] = arr2[j]
			j += 1
		k += 1

	while i < len(arr1):
		arr[k] = arr1[i]
		i += 1
		k += 1

	while j < len(arr2):
		arr[k] = arr2[j]
		j += 1
		k += 1

	return 

def merge_sort(arr):

	if len(arr) == 1:
		return arr

	mid = len(arr) // 2

	left = arr[:mid] #left array
	right = arr[mid:] #right array

	merge_sort(left)
	merge_sort(right)

	merge_sorted(left, right, arr)


arr = [2, 1, 5, 8, 9, 6, 7, 4]
merge_sort(arr)
print(arr)












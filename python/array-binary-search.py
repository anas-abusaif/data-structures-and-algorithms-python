arr=[4, 8, 15, 16, 23, 42]

def BinarySearch(numbers, value):
	low = 0
	high = len(numbers) -1

	while low <= high:
		middle = low + (high - low) // 2

		if numbers[middle] == value:
			return middle
		elif numbers[middle] < value:
			low = middle + 1
		else:
			high = middle - 1
	return -1


print(BinarySearch(arr,16))




def merge(arr1, arr2):
	"""merge two sorted arrays"""
	n1 = len(arr1)
	n2 = len(arr2)
	ret_arr = [0] * (n1 + n2)

	i = 0 
	j = 0 
	k = 0 

	while i < n1 and j < n2:
		if arr1[i] < arr2[j]:
			ret_arr[k] = arr1[i]
			i += 1
		else:
			ret_arr[k] = arr2[j] 
			j += 1
		k += 1
	
	# remaining values 
	while i < n1:
		ret_arr[k] = arr1[i]
		i += 1
		k += 1
	
	while j < n2:
		ret_arr[k] = arr2[j] 
		j += 1
		k += 1
	
	return ret_arr


def main():
	arr1 = [1,3,7]
	arr2 = [2,4,9]

	print(merge(arr1, arr2))




if __name__ == "__main__":
	main()

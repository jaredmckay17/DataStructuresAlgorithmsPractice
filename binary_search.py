# Non-recrusive implementation 

def binary_search(input_array, value):
    first = 0
    last = len(input_array) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if input_array[midpoint] == value:
            return midpoint
        else:
	    if value < input_array[midpoint]:
	        last = midpoint - 1
	    else:
	        first = midpoint + 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 19
test_val2 = 2
print binary_search(test_list, test_val1) # 5
print binary_search(test_list, test_val2) # -1

# Recursive implementation 

def binary_search(input_array, value):
    if len(input_array) == 0:
        return False
    else:
        midpoint = len(input_array) // 2
        if input_array[midpoint] == value:
            return midpoint
        else:
            if value < input_array[midpoint]:
                return binary_search(input_array[:midpoint], value)
            else:
                return binary_search(input_array[midpoint + 1:], value)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))


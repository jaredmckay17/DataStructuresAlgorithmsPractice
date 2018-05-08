# Implementation of bubble sort, which runs in O(N^2) worst case and average case, with a best case of O(N). 
# It should also be noted that this is an in-place sorting algorithm, so space complexity is constant, or O(1)

def bubble_sort(input_list):
    for number in range(len(input_list) - 1, 0, -1):
        for i in range(number):
            if input_list[i] > input_list[i + 1]:
                temp = input_list[i]
                input_list[i] = input_list[i + 1]
                input_list[i + 1] = temp


sample_data = [54,26,93,17,77,31,44,55,20]
bubble_sort(sample_data)
print(sample_data)
# [17, 20, 26, 31, 44, 54, 55, 77, 93]

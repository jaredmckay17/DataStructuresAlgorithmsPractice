# Quick sort implementation in Python derived from 'Cracking the Coding Interview' example in Java / C++

def quick_sort_driver(input_list):
    quick_sort(input_list, 0, len(input_list) - 1)


def quick_sort(input_list, first, last):
    if first < last:
        split_point = partition(input_list, first, last)
        quick_sort(input_list, first, split_point - 1)
        quick_sort(input_list, split_point + 1, last)


def partition(input_list, first, last):
    pivotvalue = input_list[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and input_list[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while input_list[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = input_list[leftmark]
            input_list[leftmark] = input_list[rightmark]
            input_list[rightmark] = temp

    temp = input_list[first]
    input_list[first] = input_list[rightmark]
    input_list[rightmark] = temp

    return rightmark


sample_data = [4, 92, 2, 912, 823, 56, 23, 98, 34, 123, 12, 324, 3]
quick_sort_driver(sample_data)
print(sample_data)
# [2, 3, 4, 12, 23, 34, 56, 92, 98, 123, 324, 823, 912]

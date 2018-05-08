def merge(first_section, second_section):
    merge_list = []
    while len(first_section) != 0 and len(second_section) != 0:
        if first_section[0] < second_section[0]:
            merge_list.append(first_section[0])
            first_section.remove(first_section[0])
        else:
            merge_list.append(second_section[0])
            second_section.remove(second_section[0])
    if len(first_section) == 0:
        merge_list += second_section
    else:
        merge_list += first_section
    return merge_list


def merge_sort(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list
    else:
        middle = len(input_list) // 2
        first_section = merge_sort(input_list[:middle])
        second_section = merge_sort(input_list[middle:])
        return merge(first_section, second_section)


sample_data = [1, 24, 7, 45, 2, 3, 11, 78, 90]
print(merge_sort(sample_data))

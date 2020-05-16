""" 
REMOVE DUPLICATES

Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; 
after removing the duplicates in-place return the new length of the array. 

Solution:
keep one pointer for iterating the array and one pointer for placing the next non-duplicate number
"""


def remove_duplicates(arr):
    last_non_duplicated_index = 0  # first pointer
    next_non_duplicated_index = 1  # last pointer

    while next_non_duplicated_index < len(arr):
        if arr[last_non_duplicated_index] != arr[next_non_duplicated_index]:
            arr[last_non_duplicated_index + 1] = arr[next_non_duplicated_index]
            last_non_duplicated_index += 1
        next_non_duplicated_index += 1

    return arr[:last_non_duplicated_index+1]


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))

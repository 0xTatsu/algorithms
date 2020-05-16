""" 
Dutch National Flag Problem 
Given an array containing 0s, 1s and 2s, sort the array in-place.

Solution:
we use 2 pointers approach (left and right)
left: keep 0
right: keep 2
index: keep 1
"""


def dutch_flag_sort(arr):
    # all elements < left are 0, and all elements > right are 2
    # all elements from >= left < i are 1
    left, right = 0, len(arr) - 1
    i = 0
    while(i <= right):
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            # increment 'i' and 'left'
            i += 1
            left += 1
        elif arr[i] == 1:
            i += 1
        else:  # the case for arr[i] == 2
            arr[i], arr[right] = arr[right], arr[i]
            # decrement 'right' only, after the swap the number at index 'i' could be 0, 1 or 2
            right -= 1


arr = [0, 1, 0, 2, 1, 0]
dutch_flag_sort(arr)
print(arr)

arr = [2, 2, 0, 1, 2, 0]
dutch_flag_sort(arr)
print(arr)

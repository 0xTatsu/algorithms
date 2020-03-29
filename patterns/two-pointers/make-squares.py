import collections


""" 
Given a sorted array, 
create a new array containing squares of all the number of the input array in the sorted order.
 """


def make_squares(arr):
    square = collections.deque()

    left = 0
    right = len(arr) - 1

    while left <= right:
        sleft = arr[left]*arr[left]
        sright = arr[right]*arr[right]
        if sleft > sright:
            square.appendleft(sleft)
            left += 1
        else:
            square.appendleft(sright)
            right -= 1

    return list(square)


print(make_squares([-2, -1, 0, 2, 3]))
print(make_squares([-3, -1, 0, 1, 2]))

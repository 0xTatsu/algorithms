import collections


""" 
Given a sorted array, 
create a new array containing squares of all the number of the input array in the sorted order.

Solution:
use two pointers starting at both the ends of the input array
whichever pointer gives us the bigger square we add it to the result array
move the pointer to the next value
 """


def make_squares(arr):
    square = [0 for x in range(len(arr))]
    left, right = 0, len(arr) - 1
    currentIndex = len(arr) - 1
    while left <= right:
        sleft = arr[left]*arr[left]
        sright = arr[right]*arr[right]
        if sleft < sright:
            square[currentIndex] = sright
            right -= 1
        else:
            square[currentIndex] = sleft
            left += 1
        currentIndex -= 1
    return square

# def make_squares(arr):
#     square = collections.deque()
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         sleft = arr[left]*arr[left]
#         sright = arr[right]*arr[right]
#         if sleft < sright:
#             square.appendleft(sright)
#             right -= 1
#         else:
#             square.appendleft(sleft)
#             left += 1
#     return list(square)


print(make_squares([-2, -1, 0, 2, 3]))
print(make_squares([-3, -1, 0, 1, 2]))

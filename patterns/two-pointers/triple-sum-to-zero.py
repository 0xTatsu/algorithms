import math


def triple_target_zero(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
            continue
        pair_target_sum(arr, -arr[i], i+1, triplets)

    return triplets


def pair_target_sum(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


# print(triple_target_zero([-3, 0, 1, 2, -1, 1, -2]) ==
#       [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])
# print(triple_target_zero([-5, 2, -1, -2, 3]) == [[-5, 2, 3], [-2, -1, 3]])


""" Time complexity #
Sorting the array will take O(N * logN)O(N∗logN). The searchPair() function will take O(N)O(N). 
As we are calling searchPair() for every number in the input array, 
this means that overall searchTriplets() will take O(N * logN + N^2)O(N∗logN+N​2​), which is asymptotically equivalent to O(N^2)O(N2).

Space complexity #
Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N)O(N) which is required for sorting. """


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while (left < right):
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # we've found a triplet with an exact sum
                return target_sum - target_diff  # return sum of all the numbers

            # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
            if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                smallest_difference = target_diff  # save the closest and the biggest difference

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum
    return target_sum - smallest_difference


print(triplet_sum_close_to_target([-2, 0, 1, 2], 2) == 1)
print(triplet_sum_close_to_target([-3, -1, 1, 2], 1) == 0)
print(triplet_sum_close_to_target([1, 0, 1, 1], 100) == 3)

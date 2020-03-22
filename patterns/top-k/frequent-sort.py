# [Medium]
# Given a string, sort it based on the decreasing frequency of its characters.
from heapq import *


def sort_character_by_frequency(str):
    count = {}
    for char in str:
        count[char] = count.get(char, 0) + 1

    maxHeap = []
    for char, freq in count.items():
        heappush(maxHeap, (-freq, char))

    res = []
    while len(maxHeap) > 1:
        res.append(maxHeap[0][1] * (-maxHeap[0][0]))
        heappop(maxHeap)
    return "".join(res)


# Complexity: O(nlogn)
""" 
The time complexity of the above algorithm is O(D*logD)
where ‘D’ is the number of distinct characters in the input string. 
This means, in the worst case, when all characters are unique 
the time complexity of the algorithm will be O(N*logN)
where ‘N’ is the total number of characters in the string. 
"""

""" 
Example 1:
Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Example 2:
Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once. """

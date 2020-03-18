from collections import Counter
import sys 

INT_MIN = -sys.maxsize -1

# There are 2 types of sliding window (Fixed & Dynamic)

# FIXED

# /**
#  * Find the max sum subarray of a fixed size K
#  *
#  * Example input:
#  * [1, 4, 2, 10, 2, 3, 1, 0, 20]
#  * k = 4
#  */

def MaxSumSubArray(arr, k): 
    currentRunningSum = 0
    maxSum = INT_MIN

    for index in range(len(arr)):
      currentRunningSum += arr[index]
      if index >= k-1:
        maxSum = max(maxSum, currentRunningSum)
        currentRunningSum -= arr[index - (k-1)]

    return maxSum

# print(MaxSumSubArray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)) 

# longest-substring-without-repeating-characters
def lengthOfLongestSubstring(s):
    hashTable = {}
    longest_length = 0
    left_window = 0

    for right_window, item in enumerate(s):
        if item in hashTable:
            if hashTable[item] > left_window: #abbbbba
                left_window = hashTable[item] + 1

        window_length = right_window - left_window + 1
        longest_length = max(longest_length, window_length)
        hashTable[item] = right_window

    return longest_length

# print(lengthOfLongestSubstring("abcbdbdbbdcdabd") == 4)


def LongestSubstringKDistinct1(arr, k):
    numberOfUnique = 0
    str_list = []
    res = []

    for item in arr:
        if item in str_list:
            str_list.append(item)
        else:
            str_list.append(item)
            numberOfUnique += 1
            while numberOfUnique > k:
                temp = str_list[0]
                str_list = str_list[1:]
                if temp not in str_list:
                    numberOfUnique -= 1
        if len(str_list) > len(res):
            res = str_list[:]

    return "".join(res)

def LongestSubstringKDistinct(arr, k):
    count = Counter()
    left_window = 0
    max_size = 0

    for right_window, item  in enumerate(arr):
        count[item] += 1
        while len(count) > k:
            count[arr[left_window]] -= 1
            if count[arr[left_window]] == 0:
                del count[arr[left_window]]
            left_window += 1
        max_size = max(max_size, right_window-left_window+1)


    return max_size
            
print(LongestSubstringKDistinct("abcbdbdbbdcdabd", 2) == 7) # bdbdbbd
# print(LongestSubstringKDistinct("abcbdbdbbdcdabd", 3) == "bcbdbdbbdcd") # bcbdbdbbdcd
# print(LongestSubstringKDistinct("abcbdbdbbdcdabd", 5) == "abcbdbdbbdcdabd") # abcbdbdbbdcdabd


# https://leetcode.com/problems/fruit-into-baskets/solution/
# https://www.youtube.com/watch?v=lkqpHmgnXSI
def totalFruit(tree):
    ans = i = 0
    count = Counter()
    for j, x in enumerate(tree):
        count[x] += 1
        while len(count) >= 3:
            count[tree[i]] -= 1
            if count[tree[i]] == 0:
                del count[tree[i]]
            i += 1
        ans = max(ans, j - i + 1)
    return ans

# print(totalFruit([1,2,1]) == 3)
# print(totalFruit([0,1,2,2]) == 3)
# print(totalFruit([1,2,3,2,2]) == 4)
# print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5)
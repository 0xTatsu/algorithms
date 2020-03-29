from collections import Counter
import sys

INT_MIN = -sys.maxsize - 1

# There are 2 types of sliding window (Fixed & Dynamic)

# FIXED

# /**
#  * Find the max sum subarray of a fixed size K
#  *
#  * Example input:
#  * [1, 4, 2, 10, 2, 3, 1, 0, 20]
#  * k = 4
#  */


""" def MaxSumSubArray(arr, k):
    currentRunningSum = 0
    maxSum = INT_MIN

    for index in range(len(arr)):
        currentRunningSum += arr[index]
        if index >= k-1:
            maxSum = max(maxSum, currentRunningSum)
            currentRunningSum -= arr[index - (k-1)]

    return maxSum """

# print(MaxSumSubArray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))

# longest-substring-without-repeating-characters
# Given a string, find the length of the longest substring without repeating characters.


""" def lengthOfLongestSubstring2(s):
    hashTable = {}
    longest_length = 0
    left_window = 0

    for right_window, item in enumerate(s):
        if item in hashTable:
            if hashTable[item] > left_window:  # abbbbba
                left_window = hashTable[item] + 1

        window_length = right_window - left_window + 1
        longest_length = max(longest_length, window_length)
        hashTable[item] = right_window

    return longest_length """


""" def lengthOfLongestSubstring(s):
    count = Counter()
    max_size = 0
    left_window = 0

    for right_window, current_char in enumerate(s):
        count[current_char] += 1
        while count[current_char] > 1:
            count[s[left_window]] -= 1
            left_window += 1
        max_size = max(max_size, right_window - left_window + 1)

    return max_size """


# print(lengthOfLongestSubstring("abcbdbdbbdcdabd") == len("abcb"))
# print(lengthOfLongestSubstring("abcabcbb") == len("abc"))


""" def LongestSubstringKDistinct(arr, k):
    count = Counter()
    left_window = 0
    max_size = 0

    for right_window, item in enumerate(arr):
        count[item] += 1
        while len(count) > k:
            count[arr[left_window]] -= 1
            if count[arr[left_window]] == 0:
                del count[arr[left_window]]
            left_window += 1
        max_size = max(max_size, right_window-left_window+1)

    return max_size """


# print(LongestSubstringKDistinct("abcbdbdbbdcdabd", 2) == 7)  # bdbdbbd
# print(LongestSubstringKDistinct("abcbdbdbbdcdabd", 3) == 11)  # bcbdbdbbdcd
# print(LongestSubstringKDistinct("abcbdbdbbdcdabd", 5)
#       == len("abcbdbdbbdcdabd"))  # abcbdbdbbdcdabd


# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# https://www.youtube.com/watch?v=ypEEgP7Hg_I
# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91272/Consise-Python-sliding-window

""" def characterReplacement(s, k):
    left = 0
    counts = Counter()
    for right, char in enumerate(s):
        counts[char] += 1
        # there are just 2 chars ABAA -> dominant char (A)
        max_char_n = counts.most_common(1)[0][1] # there is only one dominance at a time
        window_size = right - left + 1
        # window_size - max_char_n = the number of less occurences of char ABAA => B => 1
        # we don't have to use while here because we increase only, so while run just one
        if window_size - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left + 1 """


# print(characterReplacement("ABAB", 2) == 4)
# print(characterReplacement("AABABBA", 1) == 4)

# https://leetcode.com/problems/fruit-into-baskets/solution/
# https://www.youtube.com/watch?v=lkqpHmgnXSI
""" def totalFruit(tree):
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
    return ans """

# print(totalFruit([1,2,1]) == 3)
# print(totalFruit([0,1,2,2]) == 3)
# print(totalFruit([1,2,3,2,2]) == 4)
# print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5)


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    res = []
    pCounter = Counter(p)
    sCounter = Counter(s[:len(p)-1])
    for i in range(len(p)-1, len(s)):
        sCounter[s[i]] += 1   # include a new char in the window
        # This step is O(1), since there are at most 26 English letters
        if sCounter == pCounter:
            res.append(i-len(p)+1)   # append the starting index
        # decrease the count of oldest char in the window
        sCounter[s[i-len(p)+1]] -= 1
        if sCounter[s[i-len(p)+1]] == 0:
            del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
    return res


# print(findAnagrams("cbaebabacd", "abc") == [0, 6])
# print(findAnagrams("abab", "ab") == [0, 1, 2])


def minWindow(s, t):
    need = Counter(t)
    missing = len(t)
    left = final_left = final_right = 0
    for right, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if not missing:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if not final_right or right - left <= final_right - final_left:
                final_left, final_right = left, right
    return s[final_left:final_right]


print(minWindow("ADOBECODEBANC", "ABC") == "BANC")

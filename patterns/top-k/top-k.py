from heapq import *
import re
from collections import Counter


def find_k_largest_numbers(nums, k):
    result = []

    for i in range(k):
        heappush(result, nums[i])

    for j in range(k, len(nums)):
        if nums[j] > result[0]:
            heappop(result)
            heappush(result, nums[j])

    return result


# print(str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3) == [5, 12, 11]))
# print(str(find_k_largest_numbers([5, 12, 11, -1, 12], 3) == [11, 12, 12]))


def topKFrequent(words, k):
    count = Counter(words)
    heap = []
    for word, freq in count.items():
        heappush(heap, (-freq, word))

    return [heappop(heap)[1] for _ in range(k)]


# print(topKFrequent(["i", "love", "leetcode", "i",
#                     "love", "coding"], 2) == ["i", "love"])


# Top K Frequently Mentioned Keywords
# https://leetcode.com/discuss/interview-question/542597/amazon-oa-2020-top-k-frequently-mentioned-keywords
def topKFrequentMentioned(k, keywords, reviews):
    keywordSet = set(k.lower() for k in keywords)

    reviewsLowerString = " ".join(reviews).lower()
    reviewsList = re.findall(r'\w+', reviewsLowerString)
    count = Counter(reviewsList)
    i = 0
    heap = []
    for word, freq in count.items():
        if word not in keywordSet:
            continue
        if i < k:
            heappush(heap, (freq, word))
        else:
            if freq >= heap[0][0]:
                heappop(heap)
                heappush(heap, (freq, word))

        i += 1
    return sorted(heap, reverse=True)  # O(klogk)

    # reviewsLowerString = " ".join(reviews).lower()
    # reviewsList = re.findall(r'\w+', reviewsLowerString)
    # count = Counter()
    # for word in reviewsList:
    #     if word in keywordSet:
    #         count[word] += 1

    # return list(count.keys())


print(topKFrequentMentioned(2, ["anacell", "cetracular", "betacellular"], reviews=[
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]))  # == ['anacell', 'betacellular']


print(topKFrequentMentioned(3, ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"], reviews=[
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular.",
]))  # == ["betacellular", "anacell"]


# d = [(13, 1), (12, 3), (11, 1), (12, 2), (13, 2)]
# print(sorted(d, key=lambda v: (v[0], v[1])))

def removeDuplicate(duplicate):
    final_list = []
    for a in duplicate:
        if not a in final_list:
            final_list.append(a)
    return final_list


# print(list(set([1, 2, 3, 5, 3, 2])))
print(removeDuplicate([1, 2, 3, 5, 3, 2]))  # => [1,2,3,5]


def getUnique(duplicate):
    seen = {}
    final_list = []
    for x in duplicate:
        if x not in seen:
            seen[x] = 1
            final_list.append(x)
        else:
            final_list.remove(x)
    return final_list


print(getUnique([1, 2, 3, 5, 3, 2]))  # => [1, 5]


def getDuplicate(duplicate):
    seen = {}
    final_list = []
    for x in duplicate:
        if x in seen:
            final_list.append(x)
        seen[x] = 1

    return final_list


# set([x for x in l if l.count(x) > 1])
print(getDuplicate([1, 2, 3, 5, 3, 2]))  # => [2, 3]


# Sort given list by frequency and remove duplicates
# The original list : [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]
# The list after sorting and removal : [2, 3, 6, 5]
# using sorted() + set() + count()
# sorting and removal of duplicates
lst = [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]
res = sorted(set(lst), key=lambda item: lst.count(item))
print(res)

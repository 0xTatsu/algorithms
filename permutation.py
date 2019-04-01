def permutation(iStr):
    if len(iStr) == 1:
        return [iStr]

    res = []
    for i in range(len(iStr)):
        first = iStr[i]
        left = iStr[:i] + iStr[i + 1:]
        innerPermutation = permutation(left)
        for j in range(len(innerPermutation)):
            res.append(first + innerPermutation[j])
    return res


me = 'hello, My name anh, ymh! mean anme, where are you? '
s = 'naem'


def firstWR(iStr, wr):
    wrPerm = permutation(wr)
    arr = iStr.split(' ')
    for w in range(len(arr)):
        if arr[w] in wrPerm:
            return arr[w]
    return None


def indexWR(iStr, wr):
    w = firstWR(iStr, wr)
    return iStr.split(' ').index(w)


print(permutation('name'))
# print(firstWR(me, s))
# print(indexWR(me, s))

import bisect


def suggestedProducts(A, word):
    A.sort()
    res, prefix, i = [], '', 0
    for c in word:
        prefix += c
        i = bisect.bisect_left(A, prefix, i)
        data = []
        for w in A[i:i+3]:
            if w.startswith(prefix):
                data.append(w)
        res.append(data)
        # res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
    return res


print(suggestedProducts(["mobile", "mouse", "moneypot",
                         "monitor", "mousepad"], word="mouse"))

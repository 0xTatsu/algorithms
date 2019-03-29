def permutation(input):
    if len(input) == 1:
        return input if isinstance(input, list) else [input]

    result = []
    for i in range(len(input)):
        first = input[i]
        rest = input[:i] + input[i + 1:]
        rest_permutation = permutation(rest)
        for p in rest_permutation:
            result.append(first + p)
    return result


sentence = 'hello, My name anh, ymh! anme, where are you? '
word = 'anme'


def firstWR(s, wd):
    perm = permutation(wd)
    arr = s.split(' ')
    for i in range(len(perm)):
        if perm[i] in arr:
            return perm[i]


def indexWR(str, wd):
    fw = firstWR(str, wd)
    if fw is not None:
        return str.find(fw)


print(firstWR(sentence, word))
print(indexWR(sentence, word))

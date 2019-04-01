# First non-repeating character
# 'GeeksforGeeks' => f
# 'GeeksQuiz' => G


def lastIndex(input, word):
    return len(input)-input[::-1].index(word)-1


def solution(str):
    for w in str:
        if (str.index(w) == lastIndex(str, w)):
            return w


print(solution('GeeksforGeeks'))
print(solution('GeeksQuiz'))

def solution(S):
    count = 0
    for item in S:
        if item == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return 0
    if count == 0:
        return 1
    return 0


S1 = "(()(())())"  # return 1
S2 = "())"  # return 0

print(solution(S1))

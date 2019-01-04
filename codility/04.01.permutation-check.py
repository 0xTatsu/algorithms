# [4,1,3,2] => 1
# [4,1,3] => 0


def solution(A):
    length = len(A)
    seen = [0]*length
    for element in A:
        if not 1 <= element <= length:
            return 0
        elif seen[element - 1] == 1:
            return 0
        seen[element-1] = 1
    return 1

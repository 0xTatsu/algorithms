def solution(S):
    if len(S) % 2 == 1:
        return 0
    stack = []
    lefts = ["[", "{", "("]
    mapping = {"]": "[", "}": "{", ")": "("}
    for item in S:
        if item in lefts:
            stack.append(item)
        else:
            if len(stack) == 0:
                return 0
            elif mapping[item] != stack.pop():
                return 0

    if len(stack) == 0:
        return 1
    return 0


S1 = "{[()()]}"  # 1
S2 = "([)()]"  # 0

print(solution(S1))

"""
N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
"""

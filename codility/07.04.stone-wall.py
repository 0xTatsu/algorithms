def solution(H):
    stack = []
    block_count = 0    # The number of needing blocks
    for height in H:
        # IF DECREASE, search in stack, => count GREATERS and remove (cannot reuse)
        while len(stack) != 0 and height < stack[-1]:
            stack.pop()
            block_count += 1
        # IF INCREASE OR STACK IS EMPTY => add to stack
        if len(stack) == 0 or height > stack[-1]:
            stack.append(height)
    # Some blocks with different heights are still in the stack.
    block_count += len(stack)
    return block_count


H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(H))  # 7

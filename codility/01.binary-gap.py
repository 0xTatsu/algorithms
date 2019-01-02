def solution(N):
    return len(max(format(N, 'b').strip('0').split('1')))

print(solution(529))
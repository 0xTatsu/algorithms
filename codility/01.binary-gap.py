# lets convert int into binary, strip trailing zeros,
# split at '1' to list,
# then find longest element in list and get this element lenght.

# 9 => 1001 => 2.
# 529 => 1000010001 => 4.
# 20 => 10100 =>  1.
# T15 => 1111 => 0


def solution(N):
    return len(max(format(N, 'b').strip('0').split('1')))


print(solution(529))

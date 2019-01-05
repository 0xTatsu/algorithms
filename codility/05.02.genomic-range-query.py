"""
- What is the minimal number?
- A, C, G and T have impact factors of 1, 2, 3 and 4, respectively
For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:
The part between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
"""


def solution(S, P, Q):
    pass


S = 'CAGCCTA'
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))  # [2, 4, 1]

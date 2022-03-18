#!/usr/bin/python3
'''
Module that solves the N Queens problem
'''

import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    N = sys.argv[1]
    if N.isdigit() is not True:
        print('N must be a number')
        sys.exit(1)
    N = int(N)
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

def backtracking(N, i=0, a=[], b=[], c=[]):
    """Generates backtracking solutions for N queens problem"""
    if i < N:
        for j in range(N):
            if j not in a and i+j not in b and i-j not in c:
                for solution in backtracking(N, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a

for solution in backtracking(N):
    answer = [[col, row] for col, row in enumerate(solution)]
    print(answer)

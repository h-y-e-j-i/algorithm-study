# https://www.acmicpc.net/problem/15650
# N과 M (1)

import sys

N, M = map(int, sys.stdin.readline().strip().split())

seq = list()
answers = list()

def DFS_backtracking(k):
    if len(seq) == M : 
        answers.append(seq[:])
        return
    
    for i in range(k, N+1):
        if i not in seq:
            seq.append(i)
            DFS_backtracking(i+1)
            seq.pop()

DFS_backtracking(1)

for ans in answers:
    print(' '.join(map(str, ans)))
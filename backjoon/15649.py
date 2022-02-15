# https://www.acmicpc.net/problem/15649
# N과 M (1)
# https://jiwon-coding.tistory.com/21

import sys

N, M = map(int, sys.stdin.readline().strip().split())

s = []
answers = list()

def DFS():
    if len(s) == M :
        answers.append(s[:])
        return
    
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            DFS()
            s.pop()

DFS()
for ans in answers : print(' '.join(map(str, ans)))
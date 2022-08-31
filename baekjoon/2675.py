# https://www.acmicpc.net/problem/2675
# 문자열 반복
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    r, s = list(sys.stdin.readline().strip().split(" "))
    r = int(r)

    for se in s:
        for _ in range(r) : print(se, end="")
# https://www.acmicpc.net/problem/1026
# 보물
import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split(" ")))
b = list(map(int, sys.stdin.readline().strip().split(" ")))

a.sort()
b.sort(reverse=True)

result = 0
for a_e, b_e in zip(a, b):
    result += a_e*b_e

print(result)
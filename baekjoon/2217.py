# https://www.acmicpc.net/problem/2217
# 로프
import sys

n = int(sys.stdin.readline().strip())
rope = list()
for _ in range(n) : rope.append(int(sys.stdin.readline().strip()))

rope.sort(reverse=True)

max_weight = 0
for idx, r in enumerate(rope):
    if r*(idx+1) > max_weight:
        max_weight = r*(idx+1)

print(max_weight)
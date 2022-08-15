# https://www.acmicpc.net/problem/12845
# 모두의 마블
import sys

n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().strip().split(" ")))
max_idx = l.index(max(l))
max_level = l[max_idx]

max_gold = 0
for idx, l_e in enumerate(l):
    if idx == max_idx : continue
    max_gold += (max_level+l_e)

print(max_gold)
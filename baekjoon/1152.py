# https://www.acmicpc.net/problem/1152
# 단어의 개수
import sys

words = sys.stdin.readline().strip().split(" ")
count = 0

for w in words:
    if w.isalpha() : count += 1
print(count)
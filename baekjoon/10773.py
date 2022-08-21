# https://www.acmicpc.net/problem/10773
# 제로
import sys

k = int(sys.stdin.readline().strip())
stack = list()

for _ in range(k):
    num = int(sys.stdin.readline().strip())
    if num == 0 : stack.pop()
    else : stack.append(num)

print(sum(stack))

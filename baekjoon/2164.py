# https://www.acmicpc.net/problem/2164
# 카드2
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque()

for i in range(1, n+1):
    queue.append(i)

idx = 0
while len(queue) > 1:
    if idx%2 == 0 :  queue.popleft()
    else : queue.append(queue.popleft())
    idx += 1

print(queue[0])


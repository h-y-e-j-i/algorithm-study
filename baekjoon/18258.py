# https://www.acmicpc.net/problem/18258
# 큐 2
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque()

for _ in range(n):
    cmd = sys.stdin.readline().strip().split(" ")
    if len(cmd) > 1:
        queue.append(cmd[1])
    else:
        if cmd[0] == "front":
            if queue : print(queue[0])
            else : print(-1)
        elif cmd[0] == "back":
            if queue : print(queue[-1])
            else : print(-1)
        elif cmd[0] == "pop": 
            if queue : print(queue.popleft())
            else : print(-1)
        elif cmd[0] == "size" : print(len(queue))
        elif cmd[0] == "empty":
            if queue : print(0)
            else : print(1)
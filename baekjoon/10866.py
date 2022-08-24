# https://www.acmicpc.net/problem/10866
# 덱
import sys
from collections import deque

d = deque()

n = int(sys.stdin.readline().strip())

for _ in range(n):
    cmd = sys.stdin.readline().strip().split(" ")
    if len(cmd) == 2:
        if cmd[0] == "push_back":
            d.append(cmd[1])
        elif cmd[0] == "push_front":
            d.appendleft(cmd[1])
    else:
        if cmd[0] == "front":
            if d : print(d[0])
            else : print(-1)
        elif cmd[0] == "back":
            if d : print(d[-1])
            else : print(-1)
        elif cmd[0] == "size":
            print(len(d))
        elif cmd[0] == "empty":
            if d : print(0)
            else : print(1)
        elif cmd[0] == "pop_front":
            if d : print(d.popleft())
            else : print(-1)
        elif cmd[0] == "pop_back":
            if d : print(d.pop())
            else : print(-1)


# https://www.acmicpc.net/problem/10828
# 스택
import sys

n = int(sys.stdin.readline().strip())
stack = list()

for _ in range(n):
    cmd = sys.stdin.readline().strip().split(" ")
    if len(cmd) > 1:
        stack.append(cmd[1])
    else:
        if cmd[0] == "top":
            if stack : print(stack[-1])
            else : print(-1)
        elif cmd[0] == "pop": 
            if stack : print(stack.pop())
            else : print(-1)
        elif cmd[0] == "size" : print(len(stack))
        elif cmd[0] == "empty":
            if stack : print(0)
            else : print(1)

    

# https://www.acmicpc.net/problem/1874
# 스택 수열
import sys

m = int(sys.stdin.readline().strip())
result_num = list()
stack = list()
cmd = list()

for _ in range(m):
    result_num.append(int(sys.stdin.readline().strip()))

idx = 0
for i in range(1, m+1):
    cmd.append("+")
    stack.append(i)

    while True:
        if not stack : break
        if stack[-1] >= result_num[idx]:
            stack.pop()
            cmd.append("-")
            #print("-")
            idx += 1
        else: break
if stack : print("NO")
else : 
    for c in cmd: print(c)  



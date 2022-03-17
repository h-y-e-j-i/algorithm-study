# https://www.acmicpc.net/problem/12852
# 1로 만들기 2

import sys

n = int(sys.stdin.readline().strip())
f = [0]*(n+1)
g = [0]*(n+1)

for i in range(2, n+1):
    if i%2==0 and i%3==0 : 
        f[i] = min(f[i-1], f[i//3], f[i//2])+1

        if min(f[i-1], f[i//3], f[i//2])==f[i-1] : g[i] = i-1
        elif min(f[i-1], f[i//3], f[i//2])==f[i//3] : g[i] = i//3
        else : g[i] = i//2
    elif i%2==0 : 
        f[i] = min(f[i-1], f[i//2])+1
        if min(f[i-1], f[i//2])==f[i-1] : g[i] = i-1
        elif min(f[i-1], f[i//2])==f[i//2] : g[i] = i//2
    elif i%3==0 : 
        f[i] = min(f[i-1], f[i//3])+1
        if min(f[i-1], f[i//3])==f[i-1] : g[i] = i-1
        elif min(f[i-1], f[i//3])==f[i//3] : g[i] = i//3
    else : 
        f[i] = f[i-1]+1
        g[i] = i-1

print(f[-1])

i = n
while i >= 1:
    print(i, end=' ')
    i = g[i]

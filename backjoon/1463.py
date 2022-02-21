# https://www.acmicpc.net/problem/1463
# 1로 만들기
import sys

n = int(sys.stdin.readline().strip())
f = [0]*(n+1)

for i in range(2, n+1):
    if i%2==0 and i%3==0 : f[i] = min(f[i-1], f[i//3], f[i//2])+1
    elif i%2==0 : f[i] = min(f[i-1], f[i//2])+1
    elif i%3==0 : f[i] = min(f[i-1], f[i//3])+1
    else : f[i] = f[i-1]+1

print(f[-1])
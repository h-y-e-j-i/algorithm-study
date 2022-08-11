# https://www.acmicpc.net/problem/11047
# 동전 0
import sys

n, k = list(map(int, sys.stdin.readline().strip().split(" ")))
coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))

coins.sort(reverse=True)

count = 0

for c in coins:
    if k//c > 0 :
        count += k//c 
        k -= (k//c * c)
    if k == 0 : break

print(count)

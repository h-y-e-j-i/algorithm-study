# https://www.acmicpc.net/problem/2559
# 수열
import sys

n, k = list(map(int, sys.stdin.readline().strip().split(" ")))
num = list(map(int, sys.stdin.readline().strip().split(" ")))
part_sum = [sum(num[:k])]

for idx in range(1, n-k+1):
    part_sum.append(part_sum[idx-1]-num[idx-1]+num[idx+k-1])

print(max(part_sum))
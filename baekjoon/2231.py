# https://www.acmicpc.net/problem/2231
# 분해합 
import sys

n = int(sys.stdin.readline())
min_result = 0

for num in range(n, -1, -1):
    num_split = [int(sn) for sn in str(num)]
    num_sum = num+sum(num_split)
    if num_sum == n : 
        min_result = num

print(min_result)


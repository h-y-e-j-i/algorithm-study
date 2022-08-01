# 예산
# https://www.acmicpc.net/problem/2512
# 이분 탐색

import sys

n = int(sys.stdin.readline().strip())
region_budget = list(map(int, sys.stdin.readline().strip().split(" ")))
total_budget = int(sys.stdin.readline().strip())
region_budget.sort()

start, end = 1, region_budget[-1]

while start<=end:
    mid = (start+end)//2
    sum_budget = 0

    result_region_budget = list()
    for rb in region_budget:
        if rb>=mid : sum_budget += mid
        else : sum_budget += rb

    if sum_budget > total_budget:
        end = mid-1
    else:
        result = mid
        start = mid+1
        
print(result)


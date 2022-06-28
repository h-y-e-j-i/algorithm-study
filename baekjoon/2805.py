# https://www.acmicpc.net/problem/2805
# 나무 자르기
# https://developoerty.tistory.com/31
import sys

N, M = map(int, input().split(" "))
tree_height = list(map(int,  input().split(" ")))
start, end = 0, max(tree_height)

while start <= end:
    mid = (start+end)//2
    log_sum = 0
    for h in tree_height:
        if h > mid : log_sum += (h-mid)
        # diff = h-mid    
        # if diff > 0 : log_sum += diff
    
    if log_sum>=M : start = mid+1
    else : end = mid-1
print(end)
    
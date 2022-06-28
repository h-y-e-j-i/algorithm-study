# https://www.acmicpc.net/problem/2805
# 나무 자르기
# https://developoerty.tistory.com/31
import sys

N, M = list(map(int, sys.stdin.readline().strip().split(" ")))
tree_height = list(map(int, sys.stdin.readline().strip().split(" ")))
start, end = 1, max(tree_height)

while start <= end:
    mid = (start+end)//2
    log = list()
    for h in tree_height:
        diff = h-mid    
        if diff < 0 : log.append(0)
        else : log.append(diff)
    
    if sum(log)>=M : start = mid+1
    else : end = mid-1
print(end)
    
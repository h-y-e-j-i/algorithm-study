# https://www.acmicpc.net/problem/3079
# 입국심사
# 이분 탐색
# 프로그래머스와 동일

import sys
n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
times = [int(sys.stdin.readline()) for _ in range(n)]

times.sort()
start, end = times[0], times[-1]*m

while start<=end:
    mid = (start+end)//2
    simsa = 0

    for t in times:
        simsa += (mid//t)
    
    if simsa >= m :
        answer = mid
        end = mid-1     
    else :
        start = mid+1

print(answer)
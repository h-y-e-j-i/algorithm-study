# https://www.acmicpc.net/problem/11279
# 최대 힙
import heapq
import sys

heap = list()
n = int(sys.stdin.readline().strip())

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)


    
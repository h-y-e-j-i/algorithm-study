# https://www.acmicpc.net/problem/1927
# 최소 힙
import heapq
import sys

heap = list()
n = int(sys.stdin.readline().strip())

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)

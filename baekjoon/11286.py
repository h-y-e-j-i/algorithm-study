# https://www.acmicpc.net/problem/11286
# 절댓값 힙
import heapq
import sys

n = int(sys.stdin.readline().strip())
heap = list()

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            print(str(heapq.heappop(heap)[1]))
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
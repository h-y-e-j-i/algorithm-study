import sys
import heapq

heap = []

n = int(sys.stdin.readline().strip())
for i in range(n):
    input_line = list(map(int, sys.stdin.readline().strip().split(" ")))

    if i == 0:
        for il in input_line:
            heapq.heappush(heap, il)
    else:
        for il in input_line:
            min_num = heapq.heappop(heap)
            if min_num < il:
                heapq.heappush(heap, il)
            else:
                heapq.heappush(heap, min_num)
print(heapq.heappop(heap))
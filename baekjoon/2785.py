# https://www.acmicpc.net/problem/2785
# 체인
# 힌트 : https://dogsavestheworld.tistory.com/135
import sys

k = int(sys.stdin.readline().strip())

smallest_size = 1
while smallest_size < k:
    smallest_size *= 2

cut_size = smallest_size
cut_sum_size = 0
cut_count = 0

while cut_sum_size != k:
    if cut_sum_size+cut_size <= k:
        cut_sum_size += cut_size

    cut_size = cut_size//2
    cut_count += 1

print(smallest_size, cut_count-1)

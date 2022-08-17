# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4
import sys

n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
num = list(map(int, sys.stdin.readline().strip().split(" ")))
part_sum = [0]
#part_sum = list()

for idx in range(n):
    part_sum.append(part_sum[idx]+num[idx])
    #if idx==0 : part_sum.append(num[idx])
    #else : part_sum.append(part_sum[idx-1]+num[idx])

for idx in range(m):
    i, j = list(map(int, sys.stdin.readline().strip().split(" ")))
    print(part_sum[j]-part_sum[i-1])
    #print(part_sum[j])
    #print(part_sum[i-1])

# https://www.acmicpc.net/problem/11660
# 구간 합 구하기 5
import sys

n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
table = [[0] for _ in range(n)]

for i in range(n):
    j = 1
    for num in list(map(int, sys.stdin.readline().strip().split(" "))):
        table[i].append(table[i][j-1]+num)   
        j += 1

for _ in range(m):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().strip().split(" ")))
    result = 0
    for i in range(x1-1, x2):
        result += (table[i][y2] - table[i][y1-1])
    
    print(result)

# https://www.acmicpc.net/problem/13458
# 시험 감독
import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split(" ")))
b, c = list(map(int, sys.stdin.readline().strip().split(" ")))

total_supervisor = 0
for a_e in a:
    total_supervisor += 1
    if a_e > b:
        total_supervisor += ((a_e-b)//c)
        if (a_e-b)%c > 0 : total_supervisor += 1

print(total_supervisor)



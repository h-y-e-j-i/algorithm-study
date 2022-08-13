# https://www.acmicpc.net/problem/22864
# 피로도
import sys

a, b, c, m = list(map(int, sys.stdin.readline().strip().split(" ")))
total_work = 0
total_time = 0
total_fatigue = 0

if m < a : print(0)
else:
    while total_time <= 23:
        # 일하는 경우
        if total_fatigue+a <= m:
            total_work += b
            total_fatigue += a
        # 쉬어야 하는 경우
        elif total_fatigue+a > m:
            total_fatigue -= c
            if total_fatigue < 0 : total_fatigue = 0

        total_time += 1


    print(total_work)

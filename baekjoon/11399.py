# https://www.acmicpc.net/problem/11399
# ATM

import sys

n = int(sys.stdin.readline().strip())
withdrawal_time = list(map(int, sys.stdin.readline().strip().split(" ")))

withdrawal_time.sort()
time_sum = 0

for idx, wt in enumerate(withdrawal_time):
    time_sum += ((len(withdrawal_time)-idx)*wt)

print(time_sum)
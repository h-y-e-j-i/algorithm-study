# https://www.acmicpc.net/problem/1439
# 뒤집기
import sys

num = [int(s) for s in sys.stdin.readline().strip()]
count = [0, 0]

for idx in range(len(num)-1):
    if num[idx] != num[idx+1]:
        count[num[idx]] += 1

if num[-2] != num[-1]:
    count[num[-1]] += 1
else:
    count[num[-2]] += 1

print(min(count))



# https://www.acmicpc.net/problem/2750
# 수 정렬하기
import sys

n = int(sys.stdin.readline().strip())
num = list()

for _ in range(n):
    num.append(int(sys.stdin.readline().strip()))

print("\n".join(map(str,sorted(num))))
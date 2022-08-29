# https://www.acmicpc.net/problem/11720
# 숫자의 합
import sys

_, num = int(sys.stdin.readline().strip()), list(map(int, sys.stdin.readline().strip()))
print(sum(num))

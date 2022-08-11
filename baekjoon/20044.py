# https://www.acmicpc.net/problem/20044
# Project Teams 
import sys

n = int(sys.stdin.readline().strip())
w = list(map(int,sys.stdin.readline().strip().split(" ")))

w.sort()
min_result = float("inf")

for idx in range(len(w)):
    if (w[idx]+w[len(w)-1-idx]) < min_result :
        min_result = w[idx]+w[len(w)-1-idx]

print(min_result)
# https://www.acmicpc.net/problem/2908
# 상수
import sys

a, b = sys.stdin.readline().strip().split(" ")
final_a = int("".join(reversed([n for n in a])))
final_b = int("".join(reversed([n for n in b])))

if final_a > final_b : print(final_a) 
else : print(final_b)
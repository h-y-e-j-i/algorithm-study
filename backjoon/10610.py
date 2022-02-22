# https://www.acmicpc.net/problem/10610
# 30
import sys

n = sys.stdin.readline().strip()
n_list = [int(i) for i in n ]

if 0 in n_list and int(n)%3==0:
    n_list = sorted(n_list, reverse=True)
    print(''.join(map(str, n_list)))
else : print(-1)
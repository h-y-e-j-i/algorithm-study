# 듣보잡
# https://www.acmicpc.net/problem/1764

import sys

n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
n_list = [sys.stdin.readline().strip() for _ in range(n)]
m_list = [sys.stdin.readline().strip() for _ in range(m)]

result = list(set(n_list) & set(m_list))
result.sort()

print(len(result))
print("\n".join(result))

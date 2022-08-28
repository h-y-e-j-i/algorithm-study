# https://www.acmicpc.net/problem/5622
# 다이얼

import sys

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
alphabet = [a for a in sys.stdin.readline().strip()]
sec = 0

for a in alphabet:
    for idx, d in enumerate(dial):
        if a in d:
            sec += (idx+3)
            break
print(sec)


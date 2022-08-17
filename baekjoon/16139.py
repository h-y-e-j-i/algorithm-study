# https://www.acmicpc.net/problem/16139
# 인간-컴퓨터 상호작용
import sys

input_str = list(map(str, sys.stdin.readline().strip()))
q = int(sys.stdin.readline().strip())

alphabet = [[0 for _ in range(len(input_str)+1)] for _ in range(97, 122+1)]


for ch in set(input_str):
    alphabet[122-ord(ch)] 
    count = 0
    for idx, s in enumerate(input_str):
        if s == ch : count  += 1
        alphabet[ord(ch)-97][idx+1] = count


for _ in range(q):
    ch, i, j =  list(sys.stdin.readline().strip().split(" "))
    i, j = int(i), int(j)
    sys.stdout.write(f"{alphabet[ord(ch)-97][j+1]-alphabet[ord(ch)-97][i]}\n")

    

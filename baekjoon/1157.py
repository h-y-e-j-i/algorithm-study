# https://www.acmicpc.net/problem/1157
# 단어 공부
import sys

word = [w for w in sys.stdin.readline().strip().lower()]
alphabet_cnt = [0 for _ in range(26)]

for alphabet in word:
    alphabet_cnt[ord(alphabet)-ord('a')] += 1

max_cnt = max(alphabet_cnt)
cnt = 0
for idx, ac in enumerate(alphabet_cnt):
    if ac == max_cnt: 
        cnt += 1
        max_alphabet = chr(ord('a')+idx)

if cnt == 1 : print(max_alphabet.upper())
else : print("?")
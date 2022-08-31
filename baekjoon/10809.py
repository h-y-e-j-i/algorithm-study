# https://www.acmicpc.net/problem/10809
# 알파벳 찾기
import sys

word = sys.stdin.readline().strip()
word.lower()

alphabet_cnt = [-1 for _ in range(26)]

for idx in range(len(word)):
    if alphabet_cnt[ord(word[idx])-ord('a')]==-1:
        alphabet_cnt[ord(word[idx])-ord('a')] = idx

print(" ".join(map(str, alphabet_cnt)))
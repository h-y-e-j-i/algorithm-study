# https://www.acmicpc.net/problem/1339
# 단어 수학
import sys
from unittest import result

n = int(sys.stdin.readline().strip())
words_list = list()
alphabets = set() # 알파벳 종류
alphabet_to_num = dict()
num_list = [0]*10
results_list = list() # 

for _ in range(n):
    words_list.append([w for w in sys.stdin.readline().strip()])
    alphabets.update([w for w in words_list[-1]])

alphabets = list(alphabets)

def DFS_backtracking(idx):
    if idx == len(alphabets):
        result = 0
        for word in words_list:
            word_to_num = 0
            for i in range(len(word)):
                word_to_num += alphabet_to_num[word[i]] * 10 ** (len(word)-i-1)
            result += word_to_num
        results_list.append(result)
        return

    for i in range(10):
        if num_list[i] != -1:
            alphabet_to_num[alphabets[idx]] = i
            num_list[i] = -1
            DFS_backtracking(idx+1)
            num_list[i] = 0

DFS_backtracking(0)
print(max(results_list))
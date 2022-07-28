# https://www.acmicpc.net/problem/10816
# 숫자 카드

import sys

n = int(sys.stdin.readline().strip())
card_num = list(map(int, sys.stdin.readline().strip().split(" ")))
card_num.sort()
card_num_idx = 0

m = int(sys.stdin.readline().strip())
find_card_num = list(map(int, sys.stdin.readline().strip().split(" ")))
find_card_num_set = list(set(find_card_num))
count_card_num = dict()
for f in find_card_num_set:
    count_card_num[f] = 0

find_card_num_set.sort()
find_card_num_idx = 0

while card_num_idx < n and  find_card_num_idx < len(find_card_num_set):
    if card_num[card_num_idx] == find_card_num_set[find_card_num_idx]:
        count_card_num[find_card_num_set[find_card_num_idx]] += 1
        card_num_idx += 1
    elif card_num[card_num_idx] > find_card_num_set[find_card_num_idx]:
        find_card_num_idx += 1
    else:
        card_num_idx += 1

for f in find_card_num:
    print(count_card_num[f], end=" ")
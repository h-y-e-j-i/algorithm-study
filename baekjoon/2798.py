# https://www.acmicpc.net/problem/2798
# 블랙잭
import sys

n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
cards = list(map(int, sys.stdin.readline().strip().split(" ")))

cards.sort()
min_diff = float("inf")

for i in range(n-2):
    card_sum = cards[i]
    if card_sum >= m : 
        card_sum -= cards[i]
        break

    for j in range(i+1, n-1):
        card_sum += cards[j]
        if card_sum >= m : 
            card_sum -= cards[j]
            break
        
        for k in range(j+1, n):
            card_sum += cards[k]
            if card_sum > m :
                card_sum -= cards[k]
                break
            else:
                if abs(card_sum-m) < min_diff:
                    min_card_sum = card_sum
                    min_diff = abs(card_sum-m)
            card_sum -= cards[k]
        card_sum -= cards[j]
    card_sum -= cards[i]

print(min_card_sum)
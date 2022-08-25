# https://www.acmicpc.net/problem/10815 
# 숫자 카드
import sys

n = int(sys.stdin.readline().strip())
n_cards = list(map(int, sys.stdin.readline().strip().split(" ")))
m = int(sys.stdin.readline().strip())
m_cards = list(map(int, sys.stdin.readline().strip().split(" ")))

result = [[card, i] for i, card in enumerate(m_cards)]
result.sort()
for i in range(m):
    result[i][0] = 0

n_cards.sort()
m_cards.sort()
# result = [(0, i) for i in range(m)]

n_idx = 0
m_idx = 0

while n_idx < n and m_idx < m:
    if n_cards[n_idx] > m_cards[m_idx]:
        m_idx += 1
    elif n_cards[n_idx] < m_cards[m_idx]:
        n_idx += 1
    else:
        result[m_idx][0] += 1
        m_idx += 1
        
result.sort(key=lambda x:x[1])

for i in range(m):
    print(result[i][0], end=" ")

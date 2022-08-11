# https://www.acmicpc.net/problem/13305 
# 주유소
import sys

n = int(sys.stdin.readline().strip())
dis = list(map(int, sys.stdin.readline().strip().split(" ")))
dis_price = [0 for _ in range(n)]
price = list(map(int, sys.stdin.readline().strip().split(" ")))

current_idx = 0

for idx, p in enumerate(price[:-1]):
    if idx == 0 :dis_price[0] = dis[0]
    elif price[current_idx]<price[idx]:
        dis_price[current_idx] += dis[idx]
    else :
        dis_price[idx] += dis[idx]
        current_idx = idx
min_total_price = 0
for dp, p in zip(dis_price, price):
    min_total_price += dp*p

print(min_total_price)


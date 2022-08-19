# https://www.acmicpc.net/problem/10986
# 나머지 합
# 참고 : https://only-wanna.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-10986%EB%B2%88-%EB%82%98%EB%A8%B8%EC%A7%80-%ED%95%A9

import sys

n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
a = list(map(int, sys.stdin.readline().strip().split(" ")))
sum_list = [0]
sum_mod = list()
mod_count = [0 for _ in range(m)]

for idx, num in enumerate(a):
    sum_list.append(sum_list[idx]+num)
    sum_mod.append(sum_list[-1]%m)
    mod_count[sum_list[-1]%m] += 1

mod_count[0] += 1

total_result = 0
for mc in mod_count:
    total_result += (mc*(mc-1))/2

print(int(total_result))

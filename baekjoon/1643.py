# https://www.acmicpc.net/problem/1654
# 랜선 자르기
# 이분 탐색 : https://wayhome25.github.io/cs/2017/04/15/cs-16/
# 참고 : https://fast-it.tistory.com/entry/1654%EB%B2%88-%EB%9E%9C%EC%84%A0%EC%9E%90%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys

k, n = list(map(int, sys.stdin.readline().strip().split(" ")))
lan_cable = list()
for _ in range(k):
    lan_cable.append(int(sys.stdin.readline()))

lan_cable.sort()
start = 1
end = max(lan_cable)

while start<=end:
    mid = (start+end)//2
    
    cnt_cable = 0
    for c in lan_cable:
        cnt_cable+=c//mid

    if cnt_cable >= n:
        start = mid+1
    else:
        end = mid-1

print(end)
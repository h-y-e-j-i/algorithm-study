# https://www.acmicpc.net/problem/2110
# 공유기 설치
# 이분탐색
# https://dundung.tistory.com/54
import sys

N, C = map(int, sys.stdin.readline().strip())

home = list()
for _ in range(N) : home.append(int(sys.stdin.readline().strip()))
home = sorted(home)

start, end = 1, home[-1]-home[0]

# 공유기의 숫자를 만족할 때 까지 집 사이의 간격으로 이분 탐색
while start<=end:
    mid = (start+end)//2

    wifi_count = 1
    home_wifi = home[0] # 공유기를 마지막으로 설치한 집
    for i in range(N):
        # 마지막으로 설치한 집과 설치할 집의 간격이 최소 간격이라면 추가 설치
        if home[i]-home_wifi>=mid :
            wifi_count += 1
            home_wifi = home[i]
        if wifi_count >= C : break
    
    if wifi_count >= C : 
        result = mid
        start = mid+1
    else : end = mid-1

print(result)



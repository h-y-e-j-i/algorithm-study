# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3
# 입국심사
# 이분 탐색
# 힌트 : https://happy-obok.tistory.com/10

def solution(n, times):
    times.sort()
    start, end = times[0], times[-1]*n

    while start<=end:
        mid = (start+end)//2
        simsa = 0

        for t in times:
            simsa += (mid//t)
        
        if simsa >= n :
            answer = mid
            end = mid-1     
        else :
            start = mid+1

    return answer

print(solution(6, [7, 10]))
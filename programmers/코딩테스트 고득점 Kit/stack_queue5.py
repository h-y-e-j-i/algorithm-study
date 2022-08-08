# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
# 같은 숫자는 싫어

def solution(arr):
    answer = []

    for idx in range(len(arr)-1):
        if arr[idx] != arr[idx+1]:
            answer.append(arr[idx])
    
    answer.append(arr[-1])

    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3
# H-index

def solution(citations):
    citations.sort()
    for h_index in range(0, citations[-1]+1):
        count1 = 0
        count2 = 0
        for c in citations:
            if c >= h_index : count1 += 1
            else : count2 += 1

        if h_index > count1 or h_index < count2:
            break

    if h_index == 0 : return 0
    else : return h_index-1

print(solution([3, 0, 6, 1, 5]	))
print(solution([3, 4, 5, 11, 15, 16, 17, 18, 19, 20]))
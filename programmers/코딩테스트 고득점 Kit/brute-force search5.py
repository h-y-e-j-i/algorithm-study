# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3
# 최소직사각형

def solution(sizes):
    max_len = list()
    min_len = list()

    for idx, s in enumerate(sizes):
        max_len.append((max(s), idx))
        min_len.append((min(s), idx))
    
    max_len.sort()
    min_len.sort()
    
    return max_len[-1][0]*min_len[-1][0]


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	))

# https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3
# 체육복
# 참고 : https://coding-grandpa.tistory.com/100
def solution(n, lost, reserve):
    _reserve = list(set(reserve)-set(lost))
    _lost = list(set(lost)-set(reserve))

    _reserve.sort()
    _lost.sort()


    for r in _reserve:
        if (r-1) in _lost:
            _lost.remove(r-1)
        elif (r+1) in _lost:
            _lost.remove(r+1)
    return n-len(_lost)
        
print(solution(5, [2, 4], 	[1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
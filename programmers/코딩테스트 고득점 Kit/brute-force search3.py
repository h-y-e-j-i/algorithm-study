# https://school.programmers.co.kr/learn/courses/30/lessons/42842?language=python3
# 카펫

def solution(brown, yellow):
    answer = list()

    for i in range(1, yellow+1):
        if yellow%i == 0:
            j = int(yellow/i)
            brown_tmp = (i+j)*2+4

            if brown == brown_tmp:
                answer = [i+2, j+2]
                answer.sort(reverse=True)
                break
    return answer

print(solution(8, 1))
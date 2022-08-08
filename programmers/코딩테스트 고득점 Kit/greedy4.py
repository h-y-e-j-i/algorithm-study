# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 구명보트

def solution(people, limit):
    answer = 0
    
    people.sort()

    left_idx, right_idx = 0, len(people)-1

    while left_idx<right_idx:
        sum_weight = people[right_idx]
        for i in range(left_idx, right_idx):
            if sum_weight+people[i] > limit:
                left_idx = i
                right_idx -= 1
                answer += 1
                break
            elif sum_weight+people[i] == limit:
                left_idx = i+1
                right_idx -= 1
                answer += 1
                break
            else :
                sum_weight += people[i]
                left_idx = i+1
        
        if left_idx == right_idx :
            answer += 1
            break
    return answer



# print(solution([70, 50, 80, 50]	, 100))
print(solution([70, 80, 50], 100))
print(solution([100,500,500,900,950], 1000 ))
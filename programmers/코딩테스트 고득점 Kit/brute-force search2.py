# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python
# 소수 찾기
# 백트랙킹

import math

def prime_number(num):
    if num in [0, 1]:
        return True

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return True
    return False

def dfs_backtracking(num_list, current_num_list, current_idxes, result_list):
    for next_idx in range(len(num_list)):
        next_num = num_list[next_idx]

        if next_idx not in current_idxes:
            current_num_list.append(next_num)
            current_idxes.append(next_idx)
            num_to_int = int("".join(current_num_list))

            if not prime_number(num_to_int) and num_to_int not in result_list:
                result_list.append(num_to_int)
            
            dfs_backtracking(num_list, current_num_list, current_idxes, result_list)
            current_num_list.pop()
            current_idxes.pop()

def solution(numbers):
    result_list = list()
    num_list = list(map(str, numbers))

    for start_idx, start_num in enumerate(num_list):
        if not prime_number(int(start_num)) and int(start_num) not in result_list :
            result_list.append(int(start_num))
        dfs_backtracking(num_list, [start_num], [start_idx], result_list)

    return len(result_list)

# print(solution("17"))
# print(solution("011"))
print(solution("1231"))
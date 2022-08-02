# https://school.programmers.co.kr/learn/courses/30/lessons/43236?language=python3
# 징검다리
# 이분 탐색

def solution(distance, rocks, n):
    rocks.append(0)
    rocks.sort()
    start, end = 1, distance

    while start<=end:
        mid = (start+end)//2
        except_rock_cnt = 0
        
        r_idx = 0
        next_idx = 1
      
        while (r_idx+next_idx) < len(rocks):
            if (rocks[r_idx+next_idx]-rocks[r_idx]) < mid:
                except_rock_cnt += 1
                next_idx += 1
            else:
                r_idx += next_idx
                next_idx = 1
        if except_rock_cnt > n:          
            end = mid-1
        else: 
            start = mid+1
            answer = mid

    return answer

print(solution(25, 	[2, 14, 11, 21, 17]	, 2))
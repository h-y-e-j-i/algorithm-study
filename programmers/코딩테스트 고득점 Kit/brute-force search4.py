# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3
# 피로도

def backtracking(current_k, current_idxes, current_dungeons, count_dungeons, dungeons):
    for idx in range(len(dungeons)):
        if idx not in current_idxes and current_k>=dungeons[idx][0]:
            current_dungeons.append(dungeons[idx])
            current_idxes.append(idx)
            count_dungeons.append(len(current_dungeons))
            current_k -= dungeons[idx][1]
            backtracking(current_k, current_idxes, current_dungeons, count_dungeons, dungeons)
            current_dungeons.pop()
            current_idxes.pop()
            current_k += dungeons[idx][1]
    
    return max(count_dungeons)
            



def solution(k, dungeons):
    count_dungeons = list()
    answer = 0

    for start_idx in range(len(dungeons)):
        count_dungeons = list()
        if dungeons[start_idx][0]<=k:       
            count_dungeons.append(1)     
            max_dungeons = backtracking(k-dungeons[start_idx][1], [start_idx], [dungeons[start_idx]], count_dungeons, dungeons)

            if answer < max_dungeons:
                answer = max_dungeons

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
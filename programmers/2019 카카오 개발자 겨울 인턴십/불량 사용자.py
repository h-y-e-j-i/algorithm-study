# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python
# 불량 사용자

import itertools

def solution(user_id, banned_id):
    answer = 0
    banned_u_ids = list()
    banned_u_id = list()

    for _ in range(len(banned_id)):
        banned_u_id.append([]) 

    for idx, b_id in enumerate(banned_id):
        for u_id in user_id:
            if len(b_id) != len(u_id) :#or u_id in banned_u_ids:
                banned = False
                pass
            else:
                banned = True
                for i, b in enumerate(b_id):
                    if b=="*" or b==u_id[i] : pass
                    else:
                        banned = False
                        break
            if banned == True : 
                banned_u_id[idx].append(u_id)
                banned_u_ids.append(u_id)

    
    result = list(itertools.product(*banned_u_id))

    result = [tuple(sorted(i)) for i in result if len(set(i))==len(banned_id)]
    result = list(set(result))

    return len(result)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
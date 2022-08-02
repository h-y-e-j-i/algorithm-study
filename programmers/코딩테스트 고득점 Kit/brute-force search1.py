

def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5,]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    supo_socre = [0, 0, 0]
    # supo_answer = dict()
    # supo_answer['1'] = 0
    # supo_answer['2'] = 0
    # supo_answer['3'] = 0

    # while len(supo1)<len(answers) : supo1 += supo1
    # while len(supo2)<len(answers) : supo2 += supo1
    # while len(supo3)<len(answers) : supo3 += supo1

    # for sp1, sp2, sp3, ans in zip(supo1, supo2, supo3, answers):
    #     if sp1 == ans : supo_answer['1'] +=1 
    #     if sp2 == ans : supo_answer['2'] +=1
    #     if sp3 == ans : supo_answer['3'] +=1

    for ans, index in zip(answers, range(len(answers))):
        if supo1[index%len(supo1)]==ans : supo_socre[0]+=1
        if supo2[index%len(supo2)]==ans : supo_socre[1]+=1
        if supo3[index%len(supo3)]==ans : supo_socre[2]+=1
    
    for sp,score in zip(range(len(supo_socre)), supo_socre):
        if score == max(supo_socre) : answer.append(sp+1)
        else : break
    
    answer.sort()
    # sorted_supo_answer = sorted(supo_answer.items(), key = lambda x: (x[1], -int(x[0])), reverse = True)
    # for sp, score in sorted_supo_answer:
    #     if score == max(supo_answer.values()) : answer.append(int(sp))
    #     else : break
    
    return answer


print(solution([1,3,2,4,2]))
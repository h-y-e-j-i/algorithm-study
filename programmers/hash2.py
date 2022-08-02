def solution(participant, completion):
    participant.sort()
    completion.sort() 
    print(participant)
    print(completion)
    for par_index in range(len(completion)):
        if participant[par_index] != completion[par_index]:
            return participant[par_index]
    return participant[len(participant)-1]
    

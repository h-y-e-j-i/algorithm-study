def solution(operations):
    answer = []
    num_list = list()

    for operation in operations:
        if operation[0] == 'I':
           num_list.append(int(operation[2:]))
           num_list.sort()
        elif num_list and operation == 'D 1':
            num_list.pop()
        elif num_list and operation == 'D -1':
            num_list.pop(0)
        if num_list:
            answer = [num_list[-1], num_list[0]]
        else : answer = [0,0]
    return answer

#print(solution(["I 7","I 5","I -5","D -1"]))
#print(solution(["I 16","D 1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
def DFS(graph, target, start_node, numbers):
    node_count = list()
    queue = list()
    expression = list()

    numbers_len = len(numbers)
    
    count = 0
    ex_sum = 0

    queue.append(start_node)
    node_count.append(1)
    

    while queue :   
        node = queue.pop()
        while node_count[len(node_count)-1] == 0:
            node_count.pop()
            ex_sum -= expression.pop()*numbers[len(node_count)-1]
        node_count[len(node_count)-1]-=1
        expression.append(node)
        ex_sum += node*numbers[len(node_count)-1]

        # if abs(node) in numbers:
        #     expression.append(node)

        if len(expression) < numbers_len:         
            node_count.append(2)
            for next_node in graph[node]:
                queue.append(next_node)
        else:
            # ex_sum = 0
            # for term in expression:
            #     ex_sum += term
            if ex_sum == target :
                count += 1

            ex_sum -= expression.pop()*numbers[len(node_count)-1]

    return count


def solution(numbers, target):
    graph = dict()

    graph[1] = list()
    graph[1].append(1)
    graph[1].append(-1)

    graph[-1] = list()
    graph[-1].append(1)
    graph[-1].append(-1)
        
    answer = 0
    for start_node in [1, -1]:
        answer += DFS(graph, target, start_node, numbers) 
    return answer

# print(solution([1, 1, 1, 1, 1], 3))

print(solution([2, 2, 3, 3, 5], 5))

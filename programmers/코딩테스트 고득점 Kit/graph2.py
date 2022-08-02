def make_graph(n, results):
    win_graph = dict()
    lose_graph = dict()

    for i in range(n):
        win_graph[i] = list()
        lose_graph[i] = list()
    
    for n1, n2 in results:
        win_graph[n1-1].append(n2-1)
        lose_graph[n2-1].append(n1-1)

    return win_graph, lose_graph

def solution(n, results):
    win_graph, lose_graph = make_graph(n, results)
    answer = 0
    
    for i in range(n):
        visit = list()
        queue = list()

        for win_result in win_graph[i]:
            queue.append(i)
            while queue : 
                node = queue.pop(0)
                if node not in visit:
                    visit.append(node)
                    for next_node in win_graph[node]:
                        if next_node not in visit and next_node not in queue:
                            queue.append(next_node)
        
        if len(visit)==n:
            answer+= 1
        else:
            queue = list()
            if win_graph[i]:
              visit.remove(i)

            for lost_result in lose_graph[i]:
                queue.append(i)
                while queue : 
                    node = queue.pop(0)
                    if node not in visit:
                        visit.append(node)
                        for next_node in lose_graph[node]:
                            if next_node not in visit and next_node not in queue:
                                queue.append(next_node)
            if len(visit)==n:
                answer+= 1
    return answer

            
            


    
    


print(solution(	5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]))
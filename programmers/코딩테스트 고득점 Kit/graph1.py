def BFS(graph, start_node, n):
    visited = list()
    queue = list()
    node_distance = [0 for _ in range(n)] 

    queue.append(start_node)
    node_distance[start_node] += 1

    while queue or len(visited)<n:       
        node = queue.pop(0) 

        if node not in visited:            
            visited.append(node)          
            
            for next_node in graph[node]:
                if node_distance[next_node] == 0:
                    queue.append(next_node)
                    node_distance[next_node] = node_distance[node]+1

            # for i in graph[node] :
            #     if i not in queue and i not in visited:
            #         queue.append(i) 
            #         add_node_count += 1

    count = 0
    print(node_distance)
    for dis in node_distance:
        if dis == max(node_distance):
            count += 1           
      
    return count

def make_graph(n, results):
    graph = dict()
    for i in range(n):
        graph[i] = list()
    
    for n1, n2 in results:
        graph[n1-1].append(n2-1)
        graph[n2-1].append(n1-1)
    return graph


def solution(n, vertex):
    matrix = make_graph(n, vertex)
    answer = BFS(matrix, 0, n)
    return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	))
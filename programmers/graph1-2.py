def BFS(graph, start_node, n):
    visited = list()
    queue = list()
    node_count = list()
    

    final_node_count = 0

    queue.append(start_node)
    node_count.append(1)

    while queue or len(visited)<n:       
        node = queue.pop(0) 
        node_count[0] -= 1
        add_node_count = 0

        if node not in visited:            
            visited.append(node)
            # if node == end_node:
            #     return count
            if node not in graph:
                pass
            else :                
                for i in graph[node] :
                    if i not in queue and i not in visited:
                        queue.append(i) 
                        add_node_count += 1
            
            if len(node_count) <= 1:
                node_count.append(add_node_count)
            else:
                node_count[1] += (add_node_count)  

        if not queue:
            return final_node_count

        if node_count[0] == 0 :
            #node_count.append(len(graph[node]))
            final_node_count = node_count[1]
            node_count.pop(0)
            
            #count += 1
      
    return final_node_count

def make_graph(n, results):
    graph = dict()
    for i in range(1,n+1):
        graph[i] = list()
    
    for n1, n2 in results:
        graph[n1].append(n2)
        graph[n2].append(n1)
    return graph


def solution(n, vertex):
    matrix = make_graph(n, vertex)
    answer = BFS(matrix, 1, n)
    return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	))
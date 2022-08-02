def BFS(matrix, start_node, n):
    visit = list()
    queue = list()
    node_count = list()
    all_node = list()


    for i in range(n):
        all_node.append(i)
    
    final_node_count = 0

    queue.append(start_node)
    all_node.remove(start_node)
    node_count.append(1)

    not_visit = all_node
 
    while queue:       
        node = queue.pop(0) 
        node_count[0] -= 1
        next_node_count = 0

        if node not in visit:
            visit.append(node)
            for i in not_visit:
                if matrix[node][i]==1 and i not in queue:
                    queue.append(i)
                    matrix[node][i] = 0
                    matrix[i][node] = 0
                    next_node_count+=1
            not_visit = list(set(all_node)-set(visit))

            if len(node_count) <= 1:
                node_count.append(next_node_count)  
            else:
                node_count[1] += next_node_count 

        if not queue :
            return final_node_count   
        elif node_count[0] == 0 :
            #node_count.append(len(graph[node]))
            node_count.pop(0)             
            final_node_count = node_count[0]
      
    return final_node_count

def make_matrix(n, vertex):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for v1, v2 in vertex:
        matrix[v1-1][v2-1] = 1
        matrix[v2-1][v1-1] = 1
    return matrix


def solution(n, vertex):
    matrix = make_matrix(n, vertex)
    answer = BFS(matrix, 0, n)
    return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	))
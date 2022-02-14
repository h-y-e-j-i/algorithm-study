def DFS(graph, start_nodes):
    
    visited = list()    
    network_count = 0

    for start_node in range(1, start_nodes+1):
        stack = list()
        
        if start_node not in visited:
            stack.append(start_node)
            network_count += 1
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.append(node)
                    for next_node in graph[node]:                                        
                        if next_node not in visited :
                            stack.append(next_node)

    return network_count

def make_graph(n, computers):
    graph = dict()
    for com in range(1, n+1): 
        if com not in graph.keys():
            graph[com] = list()
        for net_com in range(n):
            if net_com!=com-1 and computers[com-1][net_com] == 1 and net_com not in graph[com] :
                graph[com].append(net_com+1)

                if net_com+1 not in graph.keys():
                    graph[net_com+1] = list()
                if com not in graph[net_com+1]:
                    graph[net_com+1].append(com)
                

    return graph

def solution(n, computers):
    graph = make_graph(n,computers)
    answer = DFS(graph,n)
    return answer
            
print(solution(6,[[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]))
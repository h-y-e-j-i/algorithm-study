import sys

def BFS(graph, start_node):
    visited = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node =  queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node in graph:
                graph[node].sort()
                queue.extend(graph[node])
    return visited

def DFS(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                graph[node].sort(reverse=True)
                stack.extend( graph[node])
    return visited

def make_graph(number_node, number_edge):
    graph = dict()
    for _ in range(number_edge):
        node1, node2 = map(int, sys.stdin.readline().split())
        if node1 not in graph:
            graph[node1] = list()
        if node2 not in graph:
            graph[node2] = list()
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph

def result_print(result):
    for num in result:
        print(num, end=' ')
    print()

number_node, number_edge, start_node = map(int, sys.stdin.readline().split())

graph = make_graph(number_node, number_edge)
result_print(DFS(graph, start_node))
result_print(BFS(graph, start_node))


    
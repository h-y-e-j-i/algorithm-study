# https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html

# 그래프 탐색이란
# 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것
# Ex) 특정 도시에서 다른 도시로 갈 수 있는지 없는지, 전자 회로에서 특정 단자와 단자가 서로 연결되어 있는지


# 깊이 우선 탐색(DFS)
# 루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법


# 깊이 우선 탐색(DFS)의 특징
# 자기 자신을 호출하는 순환 알고리즘의 형태 를 가지고 있다.
# 전위 순회(Pre-Order Traversals)를 포함한 다른 형태의 트리 순회는 모두 DFS의 한 종류이다.
# 이 알고리즘을 구현할 때 가장 큰 차이점은, 그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사 해야 한다는 것이다.
# 이를 검사하지 않을 경우 무한루프에 빠질 위험이 있다.

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
    for _ in number_edge:
        node1, node2 = map(int, sys.stdin.readline().split())
        if node1 not in graph:
            graph[node1] = list()
        if node2 not in graph:
            graph[node2] = list()
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph


def make_graph_local(number_node, number_edge, input_array):
    graph = dict()   
    for _ in range(number_edge):
        input_array_line = input_array.pop(0)
        node1, node2 = input_array_line[0], input_array_line[1]
        if node1 not in graph:
            graph[node1] = list()
        if node2 not in graph:
            graph[node2] = list()
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph

    
if __name__ == "__main__":

    
    # input_array = [[4, 5, 1],
    #                 [1, 2],
    #                 [1, 3],
    #                 [1, 4],
    #                 [2, 4],
    #                 [3, 4]]

    # input_array = [[5, 5, 3],
    #                 [5, 4],
    #                 [5, 2],
    #                 [1, 2],
    #                 [3, 4],
    #                 [3, 1]]

    # input_array = [[1000, 1, 1000],
    #                 [999, 1000]]

    # input_array_line = input_array.pop(0)
    # number_node = input_array_line[0]
    # number_edge = input_array_line[1]
    # start_node  = input_array_line[2]

    number_node, number_edge, start_node = map(int, sys.stdin.readline().split())
    
    graph = make_graph(number_node, number_edge)
    print(graph)
    print(DFS(graph, start_node))
    print(BFS(graph, start_node))
    

    # graph = {
    #     'A': ['B'],
    #     'B': ['A', 'C', 'H'],
    #     'C': ['B', 'D'],
    #     'D': ['C', 'E', 'G'],
    #     'E': ['D', 'F'],
    #     'F': ['E'],
    #     'G': ['D'],
    #     'H': ['B', 'I', 'J', 'M'],
    #     'I': ['H'],
    #     'J': ['H', 'K'],
    #     'K': ['J', 'L'],
    #     'L': ['K'],
    #     'M': ['H']
    # }
    
    #print(DFS(graph, 'A'))


    
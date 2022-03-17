import sys

def BFS(graph, start_node, end_node):
    visited = list()
    queue = list()
    node_count = list()
    count = 1

    queue.append(start_node)
    node_count.append(1)

    while queue:
        node =  queue.pop(0)
        node_count[0] -= 1        

        if node == 16:
             a = 3     

        if node == end_node:
            #count += len(node_count)-1
            return count


        if node not in visited:            
            visited.append(node)
            # if node == end_node:
            #     return count
            if node not in graph:
                pass
            else :                
                queue.extend(graph[node])    
            
            if len(node_count) <= 1:
                node_count.append(len(graph[node]))  
            else:
                node_count[1] += len(graph[node])   

        if node_count[0] == 0 :
            #node_count.append(len(graph[node]))
            node_count.pop(0)
            count += 1
            #count += 1
                   
def can_I_move(graph, index, temp_index, temp_node):
    if temp_node == 1:
        graph[index].append(temp_index)
    return graph

if __name__ == "__main__":
    graph = dict()
    size_x, size_y = map(int, sys.stdin.readline().split())

    maze = [list(map(int, input())) for _ in range(size_x)]
    
    for x in range(size_x):
        for y in range(size_y):
            index = x*size_y+y
            if maze[x][y] == 1:
                graph[index] = list()
                if x-1 >= 0:
                    graph = can_I_move(graph, index, size_y*(x-1)+y, maze[x-1][y])
                if x+1 < size_x:
                    graph = can_I_move(graph, index, size_y*(x+1)+y, maze[x+1][y])
                if y-1 >= 0:
                    graph = can_I_move(graph, index, size_y*(x)+(y-1), maze[x][y-1])
                if y+1 < size_y:
                    graph = can_I_move(graph, index, size_y*(x)+(y+1), maze[x][y+1])
    
    print(BFS(graph, 0, size_x*size_y-1))
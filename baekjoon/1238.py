# https://www.acmicpc.net/problem/1238
# 파티
# 다익스트라 알고리즘
import sys
import heapq

def dijkstra(start_node):
    queue = list()

    distance = [float("inf") for _ in range(n+1)]
    distance[start_node] = 0
    heapq.heappush(queue, (0, start_node))

    while queue:
        current_t, current_node = heapq.heappop(queue)
        if distance[current_node] < current_t : continue
        
        for next_node, next_t in graph[current_node]:
            if distance[current_node]+next_t < distance[next_node]:
                distance[next_node] = distance[current_node]+next_t
                heapq.heappush(queue, (distance[current_node]+next_t, next_node))

    return distance
    

n, m, x = list(map(int, sys.stdin.readline().strip().split(" ")))
t_map = list()
t_map.append(list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(m))
graph = [[] for _ in range(n+1)]

for _ in range(m):
    input_start_node, input_end_node, input_t = list(map(int, sys.stdin.readline().strip().split(" ")))
    graph[input_start_node].append((input_end_node, input_t))

end_to_town_distance = dijkstra(x)
t_list = list()
for town in range(1, n+1):
    if town == x: continue

    town_distance = dijkstra(town)
    t_list.append(town_distance[x]+end_to_town_distance[town])

print(max(t_list))

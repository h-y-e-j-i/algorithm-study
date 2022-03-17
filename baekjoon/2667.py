# https://www.acmicpc.net/problem/2667

import sys

complex_list = list()

graph = dict()

map_size = int(input())
map = list()
for _ in range(map_size):
    map.append([int(i) for i in sys.stdin.readline().strip()])
    
for i in range(map_size):
    for j in range(map_size):
        if map[i][j]==1 :
            graph[f"{i} {j}"] = list()

            if i-1>=0 and map[i-1][j] == 1 : graph[f"{i} {j}"].append(f"{i-1} {j}")
            if i+1<map_size and map[i+1][j] == 1 : graph[f"{i} {j}"].append(f"{i+1} {j}")
            if j-1>=0 and map[i][j-1] == 1 : graph[f"{i} {j}"].append(f"{i} {j-1}")
            if j+1<map_size and map[i][j+1] == 1 : graph[f"{i} {j}"].append(f"{i} {j+1}")

apartment = list(graph.keys())
visit = list()
stack = list()

while apartment:
    apartment_count = 0
    stack.append(apartment[0])
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            apartment.remove(node)
            stack.extend(graph[node])
            apartment_count += 1
    complex_list.append(apartment_count)

complex_list.sort()
print(len(complex_list))
for i in complex_list : print(i)







# 알고스팟
# BFS
# https://www.acmicpc.net/problem/1261

from collections import deque
import heapq
import sys




m, n = list(map(int, sys.stdin.readline().split(" ")))
dxs = [0, 0, 1, -1]
dys = [1, -1,0, -0]


distance = [[float("inf") for _ in range(m)] for _ in range(n)]
graph = [[[] for _ in range(m)] for _ in range(n)]
maze = list()

for _ in range(n):
    maze.append([int(wall) for wall in sys.stdin.readline().strip()])

for i in range(n):
    for j in range(m):
        for dx, dy in zip(dxs, dys):
            if (0<=i+dx<n) and (0<=j+dy<m):
                graph[i][j].append(((i+dx, j+dy), maze[i+dx][j+dy]))


queue = deque()
visited = list()
queue.append((0, 0))

def dijkstra():
    q = [] 
    heapq.heappush(q, (0, (0, 0)))
    distance[0][0] = 0

    while q:
        dist, now = heapq.heappop(q)
        now_x, now_y = now
        if distance[now_x][now_y] < dist: continue

        for next_node, next_dis in graph[now_x][now_y]:
            cost = dist+next_dis
            next_x, next_y = next_node
            if cost < distance[next_x][next_y]:
                distance[next_x][next_y] = cost
                heapq.heappush(q, (cost, next_node))


dijkstra()

print(distance[n-1][m-1])


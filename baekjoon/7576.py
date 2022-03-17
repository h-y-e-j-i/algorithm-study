# https://www.acmicpc.net/problem/7576
# 토마토

import sys
from collections import deque

queue = deque()
visit = list()

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

ripping = False
ripe_day = 0

size_M, size_N = list(map(int, sys.stdin.readline().strip().split()))
tomato_box = list()
for _ in range(size_N):
    tomato_box.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(size_N):
    for j in range(size_M): 
        if tomato_box[i][j] == 1: queue.append([i, j])       


while queue:
    node = queue.popleft()
    tomato_x, tomato_y = node

    for dx, dy in zip(dxs, dys):
        new_tomato_x, new_tomato_y = tomato_x+dx, tomato_y+dy
        if new_tomato_x>=0 and new_tomato_x<size_N \
            and new_tomato_y>=0 and new_tomato_y<size_M \
            and tomato_box[new_tomato_x][new_tomato_y] == 0:
            tomato_box[new_tomato_x][new_tomato_y] = tomato_box[tomato_x][tomato_y]+1
            queue.append([new_tomato_x, new_tomato_y])
            ripping = True

        if ripping:
            ripe_day = tomato_box[tomato_x][tomato_y]
            ripping = False

full_tomato = True
for i in range(size_N):
    for j in range(size_M): 
        if tomato_box[i][j] == 0 : 
            full_tomato = False
            break

if not full_tomato : print(-1)
else : print(ripe_day)
                        

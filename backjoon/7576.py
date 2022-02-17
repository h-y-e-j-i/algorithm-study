# https://www.acmicpc.net/problem/7576
# 토마토

import sys

tomato_grpah = dict()
ripe_tomatoes = list() # 익은 토마토 위치

size_M, size_N = list(map(int, sys.stdin.readline().strip().split()))
tomato_box = list()
for _ in range(size_N):
    tomato_box.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(size_M):
    for j in range(size_N):
        tomato_grpah[f'{i} {j}'] = list()
        if tomato_box[i][j] in [0, 1]:
            if tomato_box[i][j] == 1 : ripe_tomatoes.append(f"{i} {j}")

            if i-1>=0 and tomato_box[i-1][j] == 0:
                tomato_grpah[f'{i} {j}'].append(f"{i-1} {j}")
            if i+1<size_M and tomato_box[i-1][j] == 0:
                tomato_grpah[f'{i} {j}'].append(f"{i+1} {j}")
            if j-1>=0 and tomato_box[i][j-1] == 0:
                tomato_grpah[f'{i} {j}'].append(f"{i} {j-1}")
            if j+1<size_N and tomato_box[i][j-1] == 0:
                tomato_grpah[f'{i} {j}'].append(f"{i} {j+1}")

if any([len(val) for val in tomato_box.values()]) == False:
    print(-1)
else:
    # 




# https://www.acmicpc.net/problem/1743
# 음식물 피하기
from gc import garbage
import sys
row, col, number_of_garbage = list(map(int, sys.stdin.readline().strip().split())) # 음식물 쓰레기 맵의 크기와 갯수 입력
garbage_map = [[0 for _ in range(col)] for _ in range(row)] # map 초기화
garbage_graph = dict() # 그래프
garbage_size_list = list() # 음식물 사이즈 정리

for _ in range(number_of_garbage):
    garbage_row, garbage_col = list(map(int, sys.stdin.readline().strip().split())) # 음식물 쓰레기 위치 입력
    garbage_map[garbage_row-1][garbage_col-1] = -1 # map에 저장
    garbage_graph[f"{garbage_row-1} {garbage_col-1}"] = list() # graph 생성

grarbage_location_list = list(garbage_graph.keys()) # 음식물 쓰레기 위치 list

for grabage_location in grarbage_location_list:
    x, y = map(int, grabage_location.split()) # 현재 음식물 쓰레기 위치
    
    # 현재 음식물 쓰레기 위치로부터 상하좌우로 있는 음식물 살피고
    # 있다면 그래프에 저장
    if x-1>=0 and garbage_map[x-1][y] == -1: 
        garbage_graph[grabage_location].append(f"{x-1} {y}")
    if x+1<row and  garbage_map[x+1][y] == -1 : 
        garbage_graph[grabage_location].append(f"{x+1} {y}")
    if y-1>=0 and  garbage_map[x][y-1] == -1 : 
        garbage_graph[grabage_location].append(f"{x} {y-1}")
    if y+1<col and  garbage_map[x][y+1] == -1:
        garbage_graph[grabage_location].append(f"{x} {y+1}")

# DFS
# 음식물 쓰레기 위치를 모두 탐색
while grarbage_location_list:
    visit = list() 
    stack = list()
    stack.append(grarbage_location_list[0])

    while stack:
        node = stack.pop()
        if node not in visit:
            # 탐색한 위치를 삭제
            grarbage_location_list.remove(node)
            visit.append(node)
            stack.extend(garbage_graph[node])
    # 탐색이 끝났다면 음식물 쓰레기 크기 저장
    garbage_size_list.append(len(visit))
    # 끊겼다면 visit 초기화

print(max(garbage_size_list))
    
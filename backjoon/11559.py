# https://www.acmicpc.net/problem/11559
# DFS

import sys

# 입력
puyo_field = list()
puyo_grpah = dict()
puyo_colors = ['Y', 'R', 'G', 'B', 'P']

for color in puyo_colors: puyo_grpah[color] = dict()

for _ in range(12):
    puyo_field.append([i for i in sys.stdin.readline().strip()])

for i in range(12):
    for j in range(6):
        if puyo_field[i][j] != '.':
            puyo_grpah[puyo_field[i][j]][f"{i} {j}"] = list()

            if i-1>=0 and puyo_field[i][j] == puyo_field[i-1][j] : 
                puyo_grpah[puyo_field[i][j]][f"{i} {j}"].append(f"{i-1} {j}")
            if i+1<12 and puyo_field[i][j] == puyo_field[i+1][j] : 
                puyo_grpah[puyo_field[i][j]][f"{i} {j}"].append(f"{i+1} {j}")
            if j-1>=0 and puyo_field[i][j] == puyo_field[i][j-1] : 
                puyo_grpah[puyo_field[i][j]][f"{i} {j}"].append(f"{i} {j-1}")
            if j+1<6 and puyo_field[i][j] == puyo_field[i][j+1]:
                puyo_grpah[puyo_field[i][j]][f"{i} {j}"].append(f"{i} {j+1}")
            
popping_puyo_count = 0
popping_puyo = True

while popping_puyo:
    popping_puyo = False
    popping_puyo_list = list()

    for color in puyo_colors:   
        if puyo_grpah[color]:
            stack = list()
            visit = list()
            
            # 뿌요 위치
            # 색깔별로 뿌요를 탐색하므로 첫 노드가 무조건 모든 뿌요와 연결되지 않음
            # 따라서 발견된 puyo는 puyo_location에서 지우면서 모든 뿌요를 탐색한다
            puyo_location = list(puyo_grpah[color].keys()) 
            puyo_linked_list = list() # 첫 노드와 이어진 뿌요 연결 리스트
            
            stack.append(puyo_location[0])

            while stack:
                node = stack.pop(0)
                if node not in visit:
                    visit.append(node)
                    puyo_location.remove(node) # 방문한 뿌요는 지운다
                    stack.extend(puyo_grpah[color][node])
                    puyo_linked_list.append(node) # 뿌요 연결 리스트에 추가
                
                # 첫 노드와 이어진 뿌요들이 끝이 났다면
                # 아직 탐색하지 않은 뿌요를 찾아보자
                if not stack :
                    if len(puyo_linked_list) >= 4 : 
                        popping_puyo = True 
                        popping_puyo_list.extend(puyo_linked_list)
                    if puyo_location:
                        puyo_linked_list = list()
                        stack.append(puyo_location[0])

    if popping_puyo : 
        popping_puyo_count += 1
        # 터트리고 필드 갱신
        for j in range(6):
            # 남아있는 뿌요만 담는다(터트릴 뿌요 좌표 리스트에 없거나 .이 아닌 경우)
            puyo_field_column = [puyo_field[i][j] for i in range(11, -1, -1) if f"{i} {j}" not in popping_puyo_list and puyo_field[i][j]!='.']
            puyo_field_column += ['.']*(12-len(puyo_field_column))
            puyo_field_column.reverse()

            for i in range(12):
                puyo_field[i][j] = puyo_field_column[i]
            
        # 그래프 갱신
        puyo_grpah = dict()
        puyo_colors = ['Y', 'R', 'G', 'B', 'P']
        for color in puyo_colors: puyo_grpah[color] = dict()    

        for i in range(12):
            for j in range(6):
                if puyo_field[i][j] != '.':
                    puyo_grpah[puyo_field[i][j]][f"{i} {j}"] = list()

                    if i-1>=0 and puyo_field[i][j] == puyo_field[i-1][j] : 
                        puyo_grpah[puyo_field[i][j]][f"{i} {j}"].append(f"{i-1} {j}")
                    if i+1<12 and puyo_field[i][j] == puyo_field[i+1][j] : 
                        puyo_grpah[puyo_field[i][j]][f"{i} {j}"].append(f"{i+1} {j}")
                    if j-1>=0 and puyo_field[i][j] == puyo_field[i][j-1] : 
                        puyo_grpah[puyo_field[i][j]][f"{i} {j}"].append(f"{i} {j-1}")
                    if j+1<6 and puyo_field[i][j] == puyo_field[i][j+1]:
                        puyo_grpah[puyo_field[i][j]][f"{i} {j}"].append(f"{i} {j+1}")
            
print(popping_puyo_count)
        
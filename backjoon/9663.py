# https://www.acmicpc.net/problem/9663
# N-Queen

import sys

n = int(sys.stdin.readline().strip())
chess_location = list()
num_of_cases = 0

# dxs = [1, -1, -1, 1]
# dys = [1, 1, -1, -1]

def DFS_backtracking(next_chess_x):
    global num_of_cases
    # 퀸 8개를 다 놨다면 서로 공격하지 않는 가능한 경우의 수
    if len(chess_location) == n :
        num_of_cases += 1
        return

    for next_chess_y in range(n):
        possible = True # 퀸을 놓을 수 있는가?
        for now_chess_x, now_chess_y in chess_location:
            # 현재 놓인 체스들의 세로 줄에 있거나 혹은 현재 놓인 체스들의 대각선 줄에 있다면 퀸이 공격당하는 위치
            if now_chess_y == next_chess_y or abs(now_chess_x-next_chess_x)==abs(now_chess_y-next_chess_y):
                possible = False
                break
        # 공격당하지 않는 위치라면
        if possible:
            chess_location.append([next_chess_x, next_chess_y]) # 위치 추가
            DFS_backtracking(next_chess_x+1) # 다음 줄 위치 찾기
            chess_location.pop() # 다음 줄 모두 탐색했다면 이번 칸은 지우고 다음 칸 탐색

DFS_backtracking(0)
print(num_of_cases)

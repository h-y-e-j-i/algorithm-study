# https://www.acmicpc.net/problem/6987
# 월드컵
import sys
from itertools import combinations


game_win, game_lose, game_draw = [0]*6, [0]*6, [0]*6 # 게임 결과 
game_vs = list(combinations([i for i in range(6)], 2)) # 게임 대결 종류 # (team A vs team B)
answers = list()

def DFS_backtracking(game_vs_index):
    global possible_game

    if game_vs_index == 15:
        # any는 모두가 0 이어야 False
        if any([any(input_win), any(input_lose), any(input_draw)]) == False:
            possible_game = 1
        return
     
    team_A, team_B = game_vs[game_vs_index]

    # team A 승리, team B 패배
    if input_win[team_A]>0 and input_lose[team_B]>0 : 
        input_win[team_A] -= 1
        input_lose[team_B] -= 1
        DFS_backtracking(game_vs_index+1) # 그 다음 팀 게임 대결로 
        input_win[team_A] += 1
        input_lose[team_B] += 1 

    # team A 패배, team B 승리
    if input_lose[team_A]>0 and input_win[team_B]>0 : 
        input_lose[team_A] -= 1
        input_win[team_B] -= 1
        DFS_backtracking(game_vs_index+1) # 그 다음 팀 게임 대결로 
        input_lose[team_A] += 1
        input_win[team_B] += 1

    # team A와 team B 무승부
    if input_draw[team_A]>0 and input_draw[team_B]>0 : 
        input_draw[team_A] -= 1
        input_draw[team_B] -= 1
        DFS_backtracking(game_vs_index+1) # 그 다음 팀 게임 대결로 
        input_draw[team_A] += 1
        input_draw[team_B] += 1


for i in range(4):
    possible_game = 0
    input_win, input_lose, input_draw = list(), list(), list()
    input_result = list(map(int, sys.stdin.readline().strip().split())) # 결과를 한 줄 씩 받아온다

    # 승, 무승부, 패 결과 저장
    for j in range(6):
        input_win.append(input_result[3*j]) 
        input_draw.append(input_result[3*j+1])
        input_lose.append(input_result[3*j+2])
    DFS_backtracking(0)
    answers.append(possible_game)

print(' '.join(map(str, answers)))





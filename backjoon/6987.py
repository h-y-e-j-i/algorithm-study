# https://www.acmicpc.net/problem/6987
# 월드컵
import sys

game_count = 0

def DFS_backtracking():
    if game_count == 15 :
        return 1
    

team_name = ['A', 'B', 'C', 'D', 'E', 'F']

for _ in range(4):
    ans = 1
    win_results, lose_results, draw_results = list(), list(), list()
    input_result = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(6):
        win_results.append([team_name[i], input_result[3*i]]) # 승만 누적
        draw_results.append(input_result[3*i+1])
        lose_results.append([team_name[i], input_result[3*i+2]]) # 패만 누적

    DFS_backtracking()




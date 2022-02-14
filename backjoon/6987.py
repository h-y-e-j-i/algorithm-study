# https://www.acmicpc.net/problem/6987
# 월드컵
import sys

answers = list()

team_name = ['A', 'B', 'C', 'D', 'E', 'F']

for _ in range(4):
    ans = 1
    win_results, lose_results, draw_results = list(), list(), list()
    input_result = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(6):
        win_results.append([team_name[i], input_result[3*i]]) # 승만 누적
        draw_results.append(input_result[3*i+1])
        lose_results.append([team_name[i], input_result[3*i+2]]) # 패만 누적

    win_results = sorted(win_results, key=lambda x:x[1], reverse=True) # 승 내림차순 정렬
    lose_results = sorted(lose_results, key=lambda x:x[1], reverse=True) # 패 기준으로 내림차순으로 정렬

    if sum(draw_results) %2 != 0 or  \
        sum([lose_score for _, lose_score in lose_results])!=sum([win_score for _, win_score in win_results]):
        ans = 0
    else:
        for win_team_name, win_score in win_results:
            lose_team_count = 0
            for lose_team_name, lose_socre in lose_results:
                if win_team_name!=lose_team_name and lose_socre>0 : lose_team_count += 1
            
            # 이긴 팀의 승 횟수가 진 횟수를 차감할 수 있는 팀보다 같거나 적으면
            # 진 팀의 진 횟수를 차감한다
            if win_score <= lose_team_count:
                lose_team_count = win_score
                for lose_index in range(len(lose_results)):
                    lose_team_name, lose_socre = lose_results[lose_index][0], lose_results[lose_index][1]

                    if win_team_name!=lose_team_name and lose_results[lose_index][1]>0 : lose_results[lose_index][1] -=1
                    
                    lose_team_count -=1
                    if lose_team_count == 0 : break

                lose_results = sorted(lose_results, key=lambda x:x[1], reverse=True) # 패 기준으로 내림차순으로 정렬
            # 그렇지 않으면 차감할 수 없으므로
            # 0 출력
            else : 
                ans = 0
                break
    answers.append(ans)

for ans in answers : print(ans, end=' ')
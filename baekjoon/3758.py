import sys

test_case_cnt = int(sys.stdin.readline().strip())
for _ in range(test_case_cnt):
    n, k, t, m = list(map(int, sys.stdin.readline().strip().split(" ")))
    team_scores = dict()
    for team_id in range(1, n+1):
        team_scores[team_id] = [[0 for _ in range(k+1)], 0, 0]

    for r in range(m):
        i, j, s = list(map(int, sys.stdin.readline().strip().split(" ")))
        if team_scores[i][0][j] < s:
            team_scores[i][0][j] = s
        team_scores[i][1] += 1

        team_scores[i][2] = r


    my_team_rank = 1
    for team_id, score in team_scores.items():
        if team_id != t:
            if sum(score[0]) > sum(team_scores[t][0]):
                my_team_rank += 1
            elif sum(score[0]) == sum(team_scores[t][0]) and score[1] < team_scores[t][1]:
                my_team_rank += 1
            elif sum(score[0]) == sum(team_scores[t][0]) and score[1] == team_scores[t][1] and score[2] < team_scores[t][2]:
                my_team_rank += 1
            else:
                pass
                

    print(my_team_rank)
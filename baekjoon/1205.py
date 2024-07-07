import sys

n, taesu_score, p = sys.stdin.readline().strip().split(" ")
n, taesu_score, p = int(n), int(taesu_score), int(p)

scores = sys.stdin.readline().strip().split(" ")

real_rank = 1
current_rank = 1
for i in range(n):
    score = int(scores[i])
    if score < taesu_score:
        break
    elif score == taesu_score:
        current_rank += 1
    else:
        current_rank += 1
        real_rank = current_rank

if p >= current_rank:
    print(real_rank)
else:
    print(-1)
import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    scores = [[] for _ in range(n+1)]
    total_scores = [999 for _ in range(n+1)]
    ranks = sys.stdin.readline().strip().split(" ")
    for idx, r in enumerate(ranks):
        r = int(r)
        scores[r].append(idx+1)
    
    worst_team = list()
    for idx, s in enumerate(scores):
        if idx > 0 and 0 < len(scores[idx]) < 6:
            worst_team.append(idx)

    real_rank = 1
    scores = [[] for _ in range(n+1)]
    for idx, r in enumerate(ranks):
        r = int(r)
        if r not in worst_team:
            scores[r].append(real_rank)
            real_rank += 1

    five_score = [999 for _ in range(n+1)]
    for idx in range(n):
        if scores[idx]:
            total_scores[idx] = sum(scores[idx][:4])
            five_score[idx] = scores[idx][4]
    
    best_score = min(total_scores)
    best_five_score = 999
    for idx, ts in enumerate(total_scores):
        if best_score == ts:
            if best_five_score > five_score[idx]:
                best_five_score = five_score[idx]
                win_team = idx

    print(win_team)
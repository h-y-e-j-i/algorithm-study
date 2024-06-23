import sys

n, game= sys.stdin.readline().strip().split(" ")
n = int(n)
ready_players = set()

for _ in range(n):
    ready_players.add(sys.stdin.readline().strip())

if game == "Y": players = 1
elif game == "F": players = 2
elif game == "O": players = 3

print(len(ready_players)//players)
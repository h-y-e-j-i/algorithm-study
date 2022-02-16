import sys

n = int(sys.stdin.readline().strip())
chess = [[0 for _ in range(n)] for _ in range(n)]
chess_location_list = list()
chess_location = list()
possible = 0

def DFS_backtracking(k):
    if len(chess_location) == n :
        possible += 1
        return

    for i in range(k, n+1):
        chess_location.append(i)
        for j in range()
        


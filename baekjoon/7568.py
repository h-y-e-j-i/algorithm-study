import sys

n = int(sys.stdin.readline().strip())
peoples = list()
bigger = [0 for _ in range(n)]

for _ in range(n):
    weight, height = sys.stdin.readline().strip().split(" ")
    weight = int(weight)
    height = int(height)
    peoples.append([weight, height])

for i in range(n):
    for j in range(i, n):
        if (peoples[i][0] > peoples[j][0] and peoples[i][1] > peoples[j][1]):
            bigger[j] += 1
        elif (peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]):
            bigger[i] += 1

for i in range(n):
    print(bigger[i]+1, end=' ')
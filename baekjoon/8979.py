import sys

n, k = sys.stdin.readline().strip().split(" ")

n = int(n)
k = int(k)

results = [[] for _ in range(n+1)]
ranks = [1 for _ in range(n+1)]

for _ in range(n):
    country, gold, silver, bronze = sys.stdin.readline().split(" ")
    country = int(country)
    gold = int(gold)
    silver = int(silver)
    bronze = int(bronze)

    results[country] = [gold, silver, bronze]

for i in range(1, n+1):
    for j in range(i, n+1):
        if (results[i][0] > results[j][0]) \
            or (results[i][0] == results[j][0] and results[i][1] > results[j][1]) \
            or (results[i][0] == results[j][0] and results[i][1] == results[j][1] and results[i][2] > results[j][2]):
            ranks[j] += 1
        elif (results[i][0] < results[j][0]) \
            or (results[i][0] == results[j][0] and results[i][1] < results[j][1]) \
            or (results[i][0] == results[j][0] and results[i][1] == results[j][1] and results[i][2] < results[j][2]):
            ranks[i] += 1

print(ranks[k])
import sys

n, m = sys.stdin.readline().strip().split(" ")
n = int(n)
m = int(m)

words = dict()

for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1 

sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for sw, _ in sorted_words:
    print(sw)


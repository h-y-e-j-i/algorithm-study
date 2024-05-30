import sys

h, w, n, m = sys.stdin.readline().split(" ")

h, w, n, m = int(h), int(w), int(n), int(m)

h_people = 0
w_people = 0

for h_idx in range(0, h, n+1):
    h_people += 1

for w_idx in range(0, w, m+1):
    w_people += 1


print(h_people*w_people)
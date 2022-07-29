# 수 찾기
# https://www.acmicpc.net/problem/1920

n = int(input())
a = list(map(int, input().strip().split(" ")))

m = int(input())
b = list(map(int, input().strip().split(" ")))

b_set = list(set(b))
cnt_b = dict()
for be in b : cnt_b[be] = 0

a.sort()
b_set.sort()

a_idx, b_idx = 0, 0


while a_idx < n and b_idx < len(b_set):
    if a_idx > n : a_idx = n-1
    if b_idx > len(b_set) : b_idx = len(b_set)-1

    if a[a_idx] == b_set[b_idx]:
        cnt_b[b_set[b_idx]] = 1
        a_idx += 1
    elif a[a_idx] > b_set[b_idx]:
        b_idx += 1
    else:
        a_idx += 1

if a[-1] == b_set[-1] : cnt_b[b_set[-1]] = 1

for be in b : print(cnt_b[be])
    

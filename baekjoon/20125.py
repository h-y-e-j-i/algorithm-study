import sys

n = int(sys.stdin.readline().strip())

pixel = list()
head = tuple()
heart = tuple()
is_head_find = -1

for i in range(n):
    line = [ch for ch in sys.stdin.readline().strip()]
    pixel.append(line)
    if '*' in line and is_head_find == -1:
        is_head_find = 0
        head = (i, line.index("*"))
        heart = (head[0]+1, head[1])

left_arm = 0
right_arm = 0
for i in range(n):
    if heart[1] > i and pixel[heart[0]][i] == '*':
        left_arm += 1
    if heart[1] < i and pixel[heart[0]][i] == '*':
        right_arm += 1

waist = 0
for i in range(i):
    if i > heart[0] and pixel[i][heart[1]] == "*":
        waist += 1

left_leg = 0
right_leg = 0
for i in range(heart[0]+waist+1, n):
    if pixel[i][heart[1]-1] == '*':
        left_leg += 1
    if pixel[i][heart[1]+1] == '*':
        right_leg += 1

print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, waist, left_leg, right_leg)
# print(right_arm)
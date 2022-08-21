# https://www.acmicpc.net/problem/9012
# 괄호 
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    left_count, right_count = 0, 0

    test_data = sys.stdin.readline().strip()
    if test_data[-1] == '(' or test_data[0] == ')':
        print("NO")
    else:
        for td in test_data:
            if td == "(" : left_count += 1
            else : right_count += 1
            if left_count < right_count:
                break
        if left_count != right_count:
            print("NO")
        else:
            print("YES")
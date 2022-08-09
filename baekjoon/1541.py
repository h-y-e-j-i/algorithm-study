# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호
# 참고 : https://puleugo.tistory.com/29

import sys

expression = sys.stdin.readline().strip()
expression_list = expression.split("-")

if expression[0] == '-' : 
    expression_list = expression_list[1:]
    sum_ex = -sum(map(int, expression_list[0].split("+")))
else : 
    sum_ex = sum(map(int, expression_list[0].split("+")))

expression_list = expression.split("-")

for e in expression_list[1:]:
    sum_ex -= sum(map(int, e.split("+")))

print(sum_ex)
# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

import sys
while True:
    current_string = ""
    flag = 0

    while True:
        input_string = sys.stdin.readline().rstrip()
        if input_string == "." : break
        elif input_string[-1] != ".":
            current_string += input_string
        else : break
    
    if input_string == "." : break

    stack = list()
    left_small, right_small = 0, 0
    left_big, right_big = 0, 0

    input_string_list = [s for s in input_string]
    for s in input_string:
        if s == "(" : stack.append("(")
        elif s == ")" : 
            if stack : 
                ch = stack.pop()
                if ch == "(" : pass
                else:
                    flag = -1
                    stack.append(ch)
            else : 
                flag = -1
                break

        elif s == "[" : stack.append("[")
        elif s == "]" : 
            if stack : 
                ch = stack.pop()
                if ch == "[" : pass
                else:
                    flag = -1
                    stack.append(ch)
            else : 
                flag = -1
                break
    if flag == -1 or stack : print("no")
    else : print("yes")

    
# https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
# 올바른 괄호

def solution(s):
    s_list = list(map(str, s))

    stack = list()

    for se in s_list:
        if se == "(" : stack.append(")")
        else : 
            if not stack : return False
            else : stack.pop()
    
    if stack : return False
    else : return True

# print(solution("()()"))
# print(solution("(())()"))
print(solution("(()("))
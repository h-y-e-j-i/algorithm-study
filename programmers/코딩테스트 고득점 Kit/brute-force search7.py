# https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3
# 모음 사전
# 백트랙킹

count = 0
flag = -1

def backtracking(current_idxes, current_word_list, vowels, answer_word):
    global flag 

    if len(current_word_list) == 5:
        return

    for next_idx in range(5):    
        if flag == 0: break

        current_idxes.append(next_idx)
        current_word_list.append(vowels[next_idx])
        current_word = "".join(current_word_list)
        global count
        count += 1

        if answer_word == current_word:
            flag = 0
            break
        backtracking(current_idxes, current_word_list, vowels, answer_word)
        current_idxes.pop()
        current_word_list.pop()
        
        if flag == 0: break
    if flag == 0 : return flag
    

def solution(word):
    vowels = ["A", "E", "I", "O", "U"]

    for start_idx in range(len(vowels)):
        global count, floag

        count += 1
        if vowels[start_idx] == word : return count
        backtracking([start_idx], [vowels[start_idx]],vowels, word)
        if flag == 0 : return count

print(solution("AAAAE"))
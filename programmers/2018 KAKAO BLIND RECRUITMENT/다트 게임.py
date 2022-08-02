# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    scores = list() # 점수
    areas = list() # 영역
    
    option_star = list() # 스타상
    option_acha = list() # 아차상
    
    # 항의 인덱스
    # 영역 문자를 발견할 때 마다 항의 인덱스가 카운팅 된다.
    # 항의 인덱스는 0부터 시작하므로
    # -1로 초기화 한다면 첫번째 for문을 돌 때 1이 더해서 0부터 시작하게 된다
    element_index = -1
    for i, letter in zip(range(len(dartResult)), dartResult):
         # 10인 경우는 1과 0으로 나뉘기 때문에 예외처리
         # 인덱스가 맨 처음이 아니고, 이 전 인덱스의 문자가 숫자이면서 현재 인덱스의 문자가 0이라면
         # 현재 인덱스의 항에 숫자를 추가한다.
         # 예) 10S8D9S => 0는 1번째 인덱스고 전 인덱스가 숫자이므로 0은 10의 0이다
         # 예) 0S8D9S => 0이 0번째 인덱스이므로 그냥 숫자 0
         # 예) 1S8D0S => 이 전의 인덱스가 옵션이므로 그냥 숫자 0
        if i>0 and dartResult[i-1].isdigit() and letter == '0' : scores[element_index+1] += letter
        elif letter.isdigit() : scores.append(letter)
        elif letter.isalpha() : 
            areas.append(letter) 
            element_index += 1 # 항 하나당 영역 하나씩 있다.
        # 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 
        # 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다.
        elif letter == '*' : 
            if element_index>0 : 
                option_star.append(element_index)
                option_star.append(element_index-1) 
            else : option_star.append(element_index)
        # 아차상(#) 당첨 시 해당 점수는 마이너스된다.
        elif letter == '#' : option_acha.append(element_index)
            
    # 스타상은 앞 인덱스도 추가했으므로 정렬이 되지 않았음
    # 따라서 정렬을 수행한다
    option_star.sort()
    
    for i, score, area in zip(range(len(scores)), scores, areas):
        
        # 영역 계산
        if area == 'S': element = int(score)
        elif area == 'D' : element = int(score)**2
        elif area == 'T' : element = int(score)**3
        
        # 옵션 계산
        # 스타상은 2번 있을 수도 있음
        for _ in range(2):
            if i in option_star:
                element *= 2
                option_star.pop(0)
        # 아차상은 한번
        if i in option_acha : element *= -1   
        
        answer += element
    return answer
# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower() # 대문자 => 소문자
    
    new_id = [ch for ch in new_id]
    
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for index in range(len(new_id)):
        ch = new_id[index]
        if not ch.isdigit() and not ch.islower() and ch not in '-_.' :
            new_id[index] = ''
    
    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id = ''.join(new_id)    
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
        
    # 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(new_id)>0 and new_id[0]=='.' : new_id = new_id[1:]
    if len(new_id)>0 and new_id[-1]=='.' : new_id = new_id[:-1]

    # 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if new_id == '' : new_id = 'a'
    
    # 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.    
    if len(new_id) >= 16 : new_id = new_id[:15]
        
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if new_id[-1]=='.' : new_id = new_id[:-1]
    
    # new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    new_id = [ch for ch in new_id]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])
    
    new_id = ''.join(new_id) 

    return new_id
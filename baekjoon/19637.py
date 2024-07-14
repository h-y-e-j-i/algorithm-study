import sys

def binary_search(scores: list,  titles:  str, character_score: int):
    start = 0
    end  = len(scores)-1


    while start<=end:
        mid  = (start+end)//2
        
        if end-start==0:
            if scores[start] >= character_score:
                return titles[start]
            else:
                return titles[start+1]
        elif scores[mid] > character_score:
            end = mid-1
        elif scores[mid] < character_score:
            start = mid+1
        else:
            return titles[mid]
    
    return titles[mid]


n, m = sys.stdin.readline().strip().split(" ")
n, m = int(n), int(m)

titles = list()
scores = list()

for idx in range(n):
    title, score = sys.stdin.readline().strip(" ").split(" ")
    score = int(score)
    
    if idx > 0 and scores[-1] == score:
        pass
    else:
        titles.append(title)
        scores.append(score)


for _ in range(m):
    character_score = int(sys.stdin.readline().strip())
    character_title = binary_search(scores=scores, titles=titles, character_score=character_score)
    print(character_title)

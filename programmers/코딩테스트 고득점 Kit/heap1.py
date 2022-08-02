import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while(True):
        min_scov1 = heapq.heappop(scoville)
        if min_scov1>=K : break 
        elif len(scoville)==0:
            answer = -1
            break             
        min_scov2 = heapq.heappop(scoville)
         
        mix_scov = min_scov1+min_scov2*2
        heapq.heappush(scoville, mix_scov)
        answer += 1
        
    return answer
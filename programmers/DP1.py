import math
def DP(N, number):

    if number==0 : return 0

    fibo = dict()
    fibo[0] = [0]

    for i in range(1, 9):        
        case_set = set()
        for case_A in range(1, i):
            case_B = i-case_A
            for A in fibo[case_A]:
                for B in fibo[case_B]:            
                    case_set.add(A+B)
                    case_set.add(A-B)
                    case_set.add(A*B)                          
                    if B > 0:
                        case_set.add(A//B)
        
        num = 0
        for j in range(i):
            num += N*math.pow(10,j) 
        case_set.add(num)

        if number in case_set:
            return i
        fibo[i] = list(case_set)
        
    return -1

def solution(N, number):
    return DP(N, number)

if __name__=="__main__":
    #print(solution(1, 11111))
    print(solution(4, 17))
    # print(solution(5,5550))
    # solution(2, 11)
    

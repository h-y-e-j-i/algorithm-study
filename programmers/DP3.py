def solution(m, n, puddles):
    a = m*n
    if a == 0: return 0

    fibo = dict()
    fibo[0] = [0]

    for i in range(1, a):
        fibo[i] = list()
        for fibo_before in fibo[i-1]:
            x = fibo_before//10
            y = fibo_before-x*10        
            if x+1 < m and y+1 < n and [x+1, y+1] not in puddles:
                fibo[i].append((x+1)*10+y)
                fibo[i].append(x*10+y+1)
            elif x+1<m and y+1>=n:
                fibo[i].append((x+1)*10+y)
            elif x+1>=m and y+1<n : 
                fibo[i].append(x*10+y+1)
        if (m-1)*10+n-1 in fibo[i] :
            return fibo[i].count((m-1)*10+n-1)

print(solution(4, 3, [[2,2]]))
print(solution(2, 2, []), 2)
print(solution(100, 100, []), 690285631)
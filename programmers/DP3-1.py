dp = list()

def fib(n, m):
    dp_x_size = len(dp[0])-1
    dp_y_size = len(dp)-1

    if n==0 and m==0 : return 0
    elif n==0 and m==1 : return 1
    elif n==1 and m==n : return 1
    elif dp[n][m] == -1 : return -1
    elif dp[n][m] == 0:
        if n < dp_y_size and m < dp_x_size:
            dp[n][m] = fib[n-1][m]+fib[n][m-1]
        elif n < dp_y_size and m == 0:
            dp[n][m] = fib[n-1][m]
        elif n == 0 and m < dp_x_size:
            dp[n][m] = fib[n][m-1]

    
    

def solution(m, n, puddles):
    print(dp)
    dp.extend([0 for _ in range(m)] for _ in range(n))
    dp[0][1] = 1
    dp[1][0] = 1
    for p_x, p_y in puddles:
        dp[p_x-1][p_y-1] = -1
    fib(n-1, m-1)

solution(4, 3, [[2,2]])
#fib(3, 4, 5)

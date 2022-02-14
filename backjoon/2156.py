import sys

def dp(n, wine):
    if n==1 : return wine[1]
    elif n==2 : return wine[1]+wine[2]
    elif n==0 : return 0

    fib = [0, wine[1], wine[1]+wine[2]]
    for i in range(3, n+1):
        num = max(fib[i-1], wine[i-1]+wine[i]+fib[i-3], fib[i-2]+wine[i])
        fib.append(num)

    return fib[-1]

if __name__=="__main__":
    loop_count = int(sys.stdin.readline())
    wine = list()
    wine.append(0)
    for _ in range(loop_count):
        wine.append(int(sys.stdin.readline()))

    print(dp(loop_count, wine))

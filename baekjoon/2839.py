import sys

if __name__=="__main__":
    answer = -1
    answers = list()
    result_num = int(sys.stdin.readline())

    q, r = divmod(result_num, 5)
    for i in range(q, -1, -1):
        temp = result_num-5*i
        if temp%3 == 0 : 
            answer = i + int(temp/3)
            break

    print(answer)


# def fib_dp(n):
#     if n in [1, 2, 4] : return 0
#     elif n in [3, 5] : return 1
    
#     fibo_array = [0, 0, 1, 0, 1]
#     for i in range(5, n):
#         num = fibo_array[i-3]+fibo_array[i-5]
#         fibo_array.append(num)
#     return fibo_array

# if __name__=="__main__":
#     answers = list()
#     result_num = int(sys.stdin.readline())

#     print(fib_dp(result_num))
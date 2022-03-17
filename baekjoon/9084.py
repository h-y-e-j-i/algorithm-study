import sys

if __name__ == "__main__":
    answers = list()
    loop_count = int(sys.stdin.readline())
    
    for _ in range(loop_count):
        coin_count = int(sys.stdin.readline())
        coin_array = map(int(sys.stdin.readline().split()))
        result = int(sys.stdin.readline())
        
        fibo_array = list()

        for coin in coin_array:
            fibo_array.append(coin)
        
        for _ in range(coin_count, result):
            

    
    for answer in answers:
        print(answer)

#(재귀-메모이제이션) 피보나치

d= [0]*100 # 한번 계산한 결과 메모이제이션(저장)하기 위한 리스트 미리 초기화

def cal(num, loop):
    count = 0

    if loop<=0 : return 0
    if d[loop]!=0 : return d[loop]

    for i in range(loop):
        d[i] = cal(num, loop-1)+cal(num, loop-2)
        if d[i] == 12 : count += 1
    return d[loop]


print(cal([1, 5, 25, 55], 8))




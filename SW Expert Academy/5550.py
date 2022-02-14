# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWWxqfhKAWgDFAW4

frog_growl = [ch for ch in "croack"]
frog_growl_index = 0
T = int(input())
frog_count = 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니1다.
for test_case in range(1, T + 1):
    input_frog_growl = input()
    if type(len(input_frog_growl)/len(frog_growl)) == float : 
        print(f"#{test_case} -1")
    else:
        for letter in input_frog_growl:
            if letter == 'k' and frog_growl_index==len(frog_growl)-1:
                

print(frog)
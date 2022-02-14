# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWbrg9uabZsDFAWQ&

# 테스트케이스 개수
T = int(input())

for test_case in range(1, T + 1):
    # N개의 줄, 방향
    n, direction = input().split() # split(" ")는 \n 이 제거 되지 않음
    n = int(n)
    tiles = []
    for _ in range(n):
        tiles.append(list(map(int, input().split(" "))))

    if direction == "up":
        for i in range(n):
            # 숫자 사이에 있는 0 제거 
            number_list = [tiles[j][i] for j in range(n) if tiles[j][i]!=0]

            for j in range(len(number_list)):
                tiles[j][i] = int(number_list[j])
            for j in range(len(number_list), n):
                tiles[j][i] = 0
        
        for i in range(n):
            for j in range(n-1):
                # 만약 그 다음 숫자와 같거나 0이라면
                if tiles[j][i] == tiles[j+1][i] :
                    # 합쳐지고 한 칸 씩 이동한다
                    tiles[j][i] *= 2
                    for k in range(j+1, n-1):
                        tiles[k][i] = tiles[k+1][i]
                    # 마지막 칸은 0
                    tiles[n-1][i] = 0
    
    elif direction == "down":
        for i in range(n):
            # 숫자 사이에 있는 0 제거 
            number_list = [tiles[j][i] for j in range(n-1, -1, -1) if tiles[j][i]!=0]

            for j in range(n-1, n-len(number_list)-1, -1):
                tiles[j][i] = number_list[n-j-1]
            for j in range(n-len(number_list)-1, -1, -1):
                tiles[j][i] = 0
        
        for i in range(n):
            for j in range(n-1, 0, -1):
                # 만약 그 다음 숫자와 같거나 0이라면
                if tiles[j][i] == tiles[j-1][i] :
                    # 합쳐지고 한 칸 씩 이동한다
                    tiles[j][i] *= 2
                    for k in range(j-1, 0, -1):
                        tiles[k][i] = tiles[k-1][i]
                    # 마지막 칸은 0
                    tiles[0][i] = 0

    elif direction == "left":
        for i in range(n):
            # 숫자 사이에 있는 0 제거 
            number_list = [tiles[i][j] for j in range(n) if tiles[i][j]!=0]

            for j in range(len(number_list)):
                tiles[i][j] = int(number_list[j])
            for j in range(len(number_list), n):
                tiles[i][j] = 0

        for i in range(n):
            for j in range(n-1):
                # 만약 그 다음 숫자와 같거나 0이라면
                if tiles[i][j] == tiles[i][j+1] :
                    # 합쳐지고 한 칸 씩 이동한다
                    tiles[i][j] *= 2
                    for k in range(j+1, n-1):
                        tiles[i][k] = tiles[i][k+1]
                    # 마지막 칸은 0
                    tiles[i][n-1] = 0

    elif direction == "right":
        for i in range(n):
            # 숫자 사이에 있는 0 제거 
            number_list = [tiles[i][j] for j in range(n-1, -1, -1) if tiles[i][j]!=0]

            for j in range(n-1, n-len(number_list)-1, -1):
                tiles[i][j] = int(number_list[n-j-1])
            for j in range(n-len(number_list)-1, -1, -1):
                tiles[i][j] = 0
        
        for i in range(n):
            for j in range(n-1, 0, -1):
                # 만약 그 다음 숫자와 같거나 0이라면
                if tiles[i][j] == tiles[i][j-1] :
                    # 합쳐지고 한 칸 씩 이동한다
                    tiles[i][j] *= 2
                    for k in range(j-1, 0, -1):
                        tiles[i][k] = tiles[i][k-1]
                    # 마지막 칸은 0
                    tiles[i][0] = 0

    print(f"#{test_case}")
    for i in range(n):
        for j in range(n):
            print(tiles[i][j], end=" ")
        print()

                    


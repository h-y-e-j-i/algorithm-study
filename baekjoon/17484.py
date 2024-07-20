import sys

n, m = list(map(int, sys.stdin.readline().strip().split(" ")))

used_fuel = list()
fuel = list()

for i in range(n):
    input_fuel = list(map(int, sys.stdin.readline().strip().split(" ")))
    fuel.append(input_fuel.copy())

    if i == 0:
        used_fuel.append(input_fuel.copy())
    else:
        used_fuel.append([[float("inf"), float("inf"), float("inf")] for _ in range(m)])

for i in range(n-1):
    for j in range(0, m):
        if i == 0:
            current_fuel = used_fuel[i][j]

            if j > 0 and used_fuel[i+1][j-1][0] > current_fuel+fuel[i+1][j-1]:
                used_fuel[i+1][j-1][0] = current_fuel+fuel[i+1][j-1]
                
            if j < m-1 and used_fuel[i+1][j+1][2] > current_fuel+fuel[i+1][j+1]:
                used_fuel[i+1][j+1][2] = current_fuel+fuel[i+1][j+1]
            
            if used_fuel[i+1][j][1] > current_fuel+fuel[i+1][j]:
                used_fuel[i+1][j][1] = current_fuel+fuel[i+1][j]

        else:
            for k in range(3):
                current_fuel = used_fuel[i][j][k]
                
                if j > 0 and k!=0 and used_fuel[i+1][j-1][0] > current_fuel+fuel[i+1][j-1]:
                    used_fuel[i+1][j-1][0] = current_fuel+fuel[i+1][j-1]

                if j < m-1 and k!=2 and used_fuel[i+1][j+1][2] > current_fuel+fuel[i+1][j+1]:
                    used_fuel[i+1][j+1][2] = current_fuel+fuel[i+1][j+1]

                if k!=1 and used_fuel[i+1][j][1] > current_fuel+fuel[i+1][j]:
                    used_fuel[i+1][j][1] = current_fuel+fuel[i+1][j]


print(min([min(uf) for uf in used_fuel[n-1]]))           


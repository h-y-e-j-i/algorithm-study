a = int(input())
b = input()

b_list = [0 for _ in range(len(b))]

for i in range(len(b)):
    b_list[i] = int(b[i])

for i in range(len(b)):
    b_num = b_list.pop()
    print(b_num*a)

print(a*int(b))


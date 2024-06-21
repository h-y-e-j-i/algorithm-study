import sys

m = int(sys.stdin.readline().strip())
s = set()

for _ in range(m):
    inputs = sys.stdin.readline().strip().split(" ")
    if len(inputs) == 2:
        command, x = inputs[0], inputs[1]
    else:
        command = inputs[0]

    if command == "add":
        s.add(x)
    elif command == "check":
        if x in s:
            print(1)
        else:
            print(0)
    elif command == "remove":
        if x in s:
            s.remove(x)
    elif command == "toggle":
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif command == "all":
        s = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
    elif command == "empty":
        s = set()
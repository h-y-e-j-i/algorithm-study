import sys

input_str = [ch for ch in sys.stdin.readline().strip()]
command_cnt = int(sys.stdin.readline().strip())
current_cursor = len(input_str)
stack = list()

for _ in range(command_cnt):
    input_command = sys.stdin.readline().strip()
    if 'L' in input_command:
        if len(input_str) > 0:
            stack.append(input_str.pop())

    elif 'D' in input_command:
        if len(stack) > 0:
            input_str.append(stack.pop())
    elif 'B' in input_command:
        if len(input_str) > 0:
            input_str.pop()
    elif 'P' in input_command:
        _, ch = input_command.split(" ")
        input_str.append(ch)

print(''.join(input_str) + ''.join(list(reversed(stack))))


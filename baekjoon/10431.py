import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    student_line = list()
    input_line = sys.stdin.readline().strip().split(" ")
    test_case = input_line[0]
    students = input_line[1:]

    walk = 0
    for student in students:
        student = int(student)
        student_line.append(student)
        if len(student_line) > 0:
            for i in range(len(student_line)-1, 0, -1):
                if student_line[i] < student_line[i-1]:
                    tmp = student_line[i]
                    student_line[i] = student_line[i-1]
                    student_line[i-1] = tmp
                    walk += 1
                else:
                    break
    
    print(test_case, walk)
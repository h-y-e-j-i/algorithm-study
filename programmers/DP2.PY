def solution(triangle):
    n = len(triangle)
    if n==0 : return triangle[0][0]

    fibo = dict()
    fibo[0] = triangle[0]

    for i in range(1, len(triangle)):
        fibo[i] = [0 for _ in range(i+1)]
        for tri_child_index, tri_child in zip(range(len(triangle[i])), triangle[i]):
            if tri_child_index == 0:
                fibo[i][0] = tri_child+fibo[i-1][0]
            elif tri_child_index == len(triangle[i])-1:
                fibo[i][-1] = tri_child+fibo[i-1][-1]
            else:
                num = tri_child+fibo[i-1][tri_child_index]
                if fibo[i][tri_child_index] < num:
                    fibo[i][tri_child_index] = num
                num = tri_child+fibo[i-1][tri_child_index-1]
                if fibo[i][tri_child_index] < num:
                    fibo[i][tri_child_index] = tri_child+fibo[i-1][tri_child_index-1]
    return max(fibo[len(fibo)-1])

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
from copy import deepcopy


def solution(triangle):
    n_triangle = deepcopy(triangle)
    for i in range(len(triangle)-1):
        for j in range(i+1):
            if n_triangle[i+1][j] < n_triangle[i][j]+triangle[i+1][j]:
                n_triangle[i+1][j] = n_triangle[i][j]+triangle[i+1][j]
            if n_triangle[i+1][j+1] < n_triangle[i][j]+triangle[i+1][j+1]:
                n_triangle[i + 1][j+1] = n_triangle[i][j] + triangle[i + 1][j+1]
    return max(n_triangle[len(triangle)-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
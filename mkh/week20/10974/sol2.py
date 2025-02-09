n = int(input())
ls = tuple(map(str,range(1,n+1)))
def dfs(depth, visited, value):
    if depth == n:
        print(' '.join(value))
        return

    for i in range(n):
        if visited[i] != 1:
            visited[i] = 1
            value[depth] = ls[i]
            dfs(depth+1, visited, value)
            visited[i] = 0

dfs(0, [0]*n, [0]*n)

n = int(input())
board = [input() for _ in range(n)]
parents = [i for i in range(n**2)]
parents_cb = [i for i in range(n**2)]

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
        return parent[x]
    return x
    
def union(x, y, parent):
    m1, m2 = find(x, parent), find(y, parent)
    if m1 != m2:
        parent[m2] = m1

for i in range(n):
    for j in range(n):
        color = board[i][j]
        if i > 0:  # 위쪽 픽셀 확인 (i < 0 대신 i > 0)
            if board[i-1][j] == color:
                union(i*n+j, (i-1)*n+j, parents)
                union(i*n+j, (i-1)*n+j, parents_cb)
            elif (board[i-1][j] == 'R' and color == 'G') or (board[i-1][j] == 'G' and color == 'R'):
                union(i*n+j, (i-1)*n+j, parents_cb)
        if j > 0:  # 왼쪽 픽셀 확인 (j < 0 대신 j > 0)
            if board[i][j-1] == color:
                union(i*n+j, i*n+(j-1), parents)
                union(i*n+j, i*n+(j-1), parents_cb)
            elif (board[i][j-1] == 'R' and color == 'G') or (board[i][j-1] == 'G' and color == 'R'):
                union(i*n+j, i*n+(j-1), parents_cb)

colors = set()
colors_cb = set()

for i in range(n):
    for j in range(n):
        colors.add(find(i*n+j, parents))
        colors_cb.add(find(i*n+j, parents_cb))

print(len(colors), len(colors_cb))
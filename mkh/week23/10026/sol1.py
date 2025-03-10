n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited_cb = [[0]*n for _ in range(n)]
deltas = ((1,0),(-1,0),(0,1),(0,-1))
ans=[0,0]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            curr = board[i][j]
            visited[i][j]=1
            ans[0]+=1

            if not visited_cb[i][j]:
                visited_cb[i][j]=1
                ans[1]+=1
            stack = [(i,j)]
            stack2 = set()
            
            while stack:
                cy, cx = stack.pop()
                visited[cy][cx]=1
                visited_cb[cy][cx]=1

                for dy, dx in deltas:
                    ny, nx = cy+dy, cx+dx
                    if 0<=ny<n and 0<=nx<n:
                        if board[ny][nx] == curr and not visited[ny][nx]:
                            stack.append((ny,nx,))
                        elif (board[ny][nx] == 'R' and curr == 'G') or (board[ny][nx] == 'G' and curr == 'R') and not visited_cb[ny][nx]:
                            stack2.add((ny,nx,))

            stack2 = list(stack2)

            while stack2:
                cy, cx = stack2.pop()
                visited_cb[cy][cx]=1

                for dy, dx in deltas:
                    ny, nx = cy+dy, cx+dx
                    if 0<=ny<n and 0<=nx<n and (board[ny][nx]==curr or (board[ny][nx] == 'R' and curr == 'G') or (board[ny][nx] == 'G' and curr == 'R')) and not visited_cb[ny][nx]:
                        stack2.append((ny,nx,))

print(' '.join(map(str,ans)))
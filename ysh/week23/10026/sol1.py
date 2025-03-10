delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs():
    visited = [[0] * n for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j]:  # 이미 방문한 곳은 건너뜀
                continue

            # 새로운 구역 탐색 시작
            stack = [(i, j)]
            visited[i][j] = 1
            color = picture[i][j]
            answer += 1  # 새로운 구역을 발견했으므로 증가

            while stack:
                y, x = stack.pop()
                for dy, dx in delta:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                        if picture[ny][nx] == color: # 시작한 칸과 같은 색 이라면
                            visited[ny][nx] = 1
                            stack.append((ny, nx))

    return answer

def dfs2():  # 적록색약 용
    visited = [[0] * n for _ in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j]:  # 이미 방문한 곳은 건너뜀
                continue

            # 새로운 구역 탐색 시작
            stack = [(i, j)]
            visited[i][j] = 1
            color = picture[i][j]
            answer += 1  # 새로운 구역을 발견했으므로 증가

            while stack:
                y, x = stack.pop()
                for dy, dx in delta:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                        # 파랑으로 같거나 둘다 파랑이 아니어서 같게 보이거나
                        if (color == "B" and picture[ny][nx] == "B") or (color != "B" and picture[ny][nx] != "B"):
                            visited[ny][nx] = 1
                            stack.append((ny, nx))

    return answer

n = int(input())  # 크기
picture = [list(input().strip()) for _ in range(n)]

answer1 = dfs()
answer2 = dfs2()

print(answer1, answer2)

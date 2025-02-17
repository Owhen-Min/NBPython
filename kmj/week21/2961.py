N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]
min_diff = 1e9  # 신맛과 쓴맛 차이의 최소값

def dfs(depth, sin, ssen, used):
    global min_diff

    # 최소 한 개 이상의 재료를 선택했을 때만 비교
    if used > 0:
        min_diff = min(min_diff, abs(sin - ssen))

    # 종료 조건 : 모든 재료 탐색 ㅇ
    if depth == N:
        return

    # 현재 재료를 선택 ㅇ
    dfs(depth + 1, sin * ingredients[depth][0], ssen + ingredients[depth][1], used + 1)

    # 현재 재료를 선택 x
    dfs(depth + 1, sin, ssen, used)

# DFS 시작 (신맛 = 1, 쓴맛 = 0, 선택한 재료 개수 = 0)
dfs(0, 1, 0, 0)

print(min_diff)

N = int(input())  # 숫자 개수
visited = [0] * N  # 방문 체크

def dfs(depth, perm):
    # 종료 조건: N개의 숫자를 모두 선택한 경우
    if depth == N:
        print(" ".join(map(str, perm)))  # 출력 형식 맞추기
        return
    
    for i in range(N):
        if not visited[i]:  # 숫자를 아직 사용하지 않았다면?
            visited[i] = 1  # 방문 체크
            dfs(depth + 1, perm + [i + 1])  # 다음 숫자 선택
            visited[i] = 0  # 다시 사용 가능하게 되돌리기


dfs(0, [])

import sys
sys.stdin = open("sample_input.txt", "r")

# 최소 합을 구하는 DFS 함수
# m : 2차원 배열, N : 배열크기, row : 현재 탐색하는 행, used_col : 사용한 열, cur_sum : 현재까지의 합
def dfs(m, N, row, used_col, cur_sum):
    # 기저조건 : 마지막 행까지 다 선택했으면 지금까지의 합을 반환
    if row == N:
        print(cur_sum)
        return cur_sum

    min_sum = 100000  # 아주 큰 값으로 설정

    # 현재 행에서 선택할 열을 정하기
    for col in range(N):
        if not used_col[col]:  # 아직 그 열을 선택하지 않았으면 (해당 열이 F라면)
            used_col[col] = True  # 그 열을 선택 표시
            result = dfs(m, N, row + 1, used_col, cur_sum + m[row][col]) # 선택한 후, 현재까지의 합을 갱신하고 다음 열을 찾기위해 다음 행 탐색 시작
            min_sum = min(min_sum, result)  # 최소값 갱신
            used_col[col] = False  # 하나의 탐색이 끝나면 다음 탐색을 위해 초기화

    return min_sum # 최종 결과

# 최소 합을 찾는 함수
def fuc_min_sum(m, N):
    used_col = [False] * N  # 각 열이 선택됐는 지 저장
    return dfs(m, N, 0, used_col, 0)  # 시작

T = int(input())
for t in range(1, T + 1):
    N = int(input())  # N : 배열 크기
    m = [list(map(int, input().split())) for _ in range(N)]  # m : NxN 배열
    result = fuc_min_sum(m, N)  # 최소 합 계산
    print(f"#{t} {result}")

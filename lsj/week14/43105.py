def solution(triangle):
    # 아래층부터 시작
    for i in range(len(triangle) - 2, -1, -1):  # 아래에서 두 번째 줄부터 시작
        for j in range(len(triangle[i])):
            # 아래층의 인접한 두 값 중 더 큰 값을 선택해 현재 값에 더하기
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    # 삼각형의 꼭대기 요소에 최대 경로 합이 저장됨
    return triangle[0][0]
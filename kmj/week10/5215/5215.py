def hamburger(i, cal,cur_score): # i : 사용된 재료 갯수 / cal : 사용한 칼로리 / cur_score : 현재까지의 점수합
    global max_score,N,L

    # 가지 치기
    if cal > L: # 제한 칼로리인 L을 넘으면 조건 위배이므로 멈추기
        return
    # 기저 조건
    if i == N : # 모든 재료를 순회한 경우
        if max_score < cur_score:
            max_score = cur_score
        return

    # 재료 사용 안 했다면
    hamburger(i+1, cal, cur_score)

    # 재료 사용 했다면
    hamburger(i+1, cal+food[i][1], cur_score+food[i][0])


T = int(input())
for tc in range(1,T+1):
    N, L = map(int,input().split()) # N : 재료 수  / L : 제한 칼로리
    food = [list(map(int,input().split())) for _ in range(N)] # food[i][0] : 맛 점수 / food[i][1] : 칼로리

    max_score = 0 # 점수가 높은 햄버거의 점수 (최종 결과)
    hamburger(0,0,0) # 사용된 재료 갯수 / 사용 가능한 칼로리 /  현재까지의 점수합

    print(f"#{tc} {max_score}")

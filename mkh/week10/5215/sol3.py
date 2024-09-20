# 메모리: 49232kb, 실행시간: 2757 ms


T = int(input())

for tc in range(1, T+1):
    N, L = map(int,input().split())
    ingredients = [list(map(int,input().split())) for _ in range(N)]
    max_score = 0
    for i in range(1<<N):
        score = 0
        calory = 0
        for j in range(N):
            if i & (1<<j):
                score += ingredients[j][0]
                calory += ingredients[j][1]
        if calory <= L and max_score < score:
            max_score = score

    print(f'#{tc} {max_score}')
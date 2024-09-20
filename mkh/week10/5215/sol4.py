# 메모리: 54292kb, 실행시간: 6435ms


from itertools import combinations


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [tuple(map(int, input().split())) for _ in range(N)]
    max_score = 0
    for r in range(1, N + 1):  # 재료의 개수 r
        for combo in combinations(ingredients, r):  # r개가 들어간 조합들에서
            score = sum(item[0] for item in combo)
            cal = sum(item[1] for item in combo)
            if cal <= L and score > max_score:  # 칼로리 내에 최고 스코어가 있다면 갱신한다
                max_score = score
    print(f'#{tc} {max_score}')
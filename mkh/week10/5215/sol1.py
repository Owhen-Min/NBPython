# 메모리: 58,196kb, 실행시간: 655 ms


def best_burger(index, calory, score, max_score=0):
    if calory > L:                      # 칼로리가 초과했다면, 기존에 있는 max_score를 반환한다. (백트래킹)
        return max_score
    elif index == N:                    # 마지막 원소까지 봤다면
        if max_score < score:           # score가 최대값일 경우 최댓값을 갱신한 후 반환한다.
            max_score = score
        return max_score
    else:                               # 마지막 원소까지 안 봤다면, 해당 인덱스에 있는 재료를 넣은 값과 안 넣은 값을 넣고 재귀를 돌린다.
        max_score = max(best_burger(index+1, calory + calories[index], score + scores[index], max_score),best_burger(index+1, calory, score, max_score))
        return max_score



T = int(input())
for tc in range(1, T+1):
    N, L = map(int,input().split())

    calories = [0]*N
    scores = [0]*N
    max_score = 0

    for i in range(N):
        T, K = map(int,input().split())
        scores[i] = T
        calories[i] = K

    print(f'#{tc} {best_burger(0, 0, 0)}')
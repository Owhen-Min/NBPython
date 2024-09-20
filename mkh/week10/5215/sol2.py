# 메모리: 208240kb, 실행시간: 10906 ms


from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, L = map(int,input().split())
    scores = []
    cals = []
    for i in range(N):
        score, cal = map(int,input().split())
        scores.append(score)
        cals.append(cal)

    max_score = 0

    for i in range(1, N+1):             # 재료에 몇 개가 들어가는지 알려주는 i
        subset_score_i = list(combinations(scores, i))          # i개의 재료가 들어간 점수 리스트
        subset_cal_i = list(combinations(cals,i))               # i개의 재료가 들어간 칼로리 리스트
        for j in range(len(subset_cal_i)):                      # i개의 재료가 들어간 점수 리스트들로 확인해서 최대값 갱신
            if sum(subset_cal_i[j]) <= L and max_score < sum(subset_score_i[j]):
                max_score = sum(subset_score_i[j])

    print(f'#{tc} {max_score}')
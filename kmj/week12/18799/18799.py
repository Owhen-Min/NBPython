def f(i, k):  # bit[i]를 결정하는 함수
    if i == N:  # 모든 원소에 대해 결정하면

        cur_sub_sum = 0 # 현재 부분집합의 합
        cur_cnt = 0 # 현재 부분집합의 길이

        # 부분집합의 평균 구하기 시작
        for j in range(k):
            if bit[j]:  # bit[j] == 1
                cur_sub_sum += set_list[j]
                cur_cnt += 1
        # 현재 부분집합의 합을 다 구하면
        # 평균 구해서 sub_avg에 저장
        if cur_cnt > 0: # 공집합이 아니면 평균 계산
            sub_avg.append(cur_sub_sum/cur_cnt)

    else:
        bit[i] = 1 # 원소 포함 ㅇ
        f(i + 1, k)
        bit[i] = 0 # 원소 포함 x
        f(i + 1, k)

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 집합 크기
    set_list = list(map(int,input().split())) # 집합의 원소

    bit = [0] * N  # 원소의 포함여부를 표시하는 배열
    sub_avg = []  # 각 부분집합의 평균 저장

    f(0, N)

     # 부분집합의 평균의 평균
    total_sum = sum(sub_avg) # 평균의 합
    result = total_sum/(len(sub_avg))

    # rstrip(): 문자열의 오른쪽 끝에서 불필요한 문자들을 제거하는 메서드
    print(f'#{tc} {result:.14f}'.rstrip('0').rstrip('.'))

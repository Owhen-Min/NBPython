def arr_min_sum(N, i, sum, used):
    global min_sum
    if sum > min_sum:                   # 이미 숫자들의 합이 최소값을 넘었다면, 재귀함수를 끝낸다.
        return
    elif i == N and min_sum > sum:      # 순회가 끝났고, min sum보다 sum이 더 작다면 값을 갱신한다.
        min_sum = sum
    else:
        for j in range(N):
            if not used[j]:             # j번째 줄을 사용하지 않았다면
                used[j] = 1             # j를 사용했다고 체크하고서
                arr_min_sum(N, i+1, sum+matrix[i][j], used)     # 다음 번째 줄로 넘긴다.
                used[j]=0               # 다음 순회를 위해 사용했다고 체크한걸 되돌린다.


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    min_sum = 0
    for i in range(N):
        min_sum += matrix[i][i]         # 최소값의 초기값을 \ 로 설정한다.
    used = [0]*N                        # 그 줄을 사용했는지 체크하는 데 사용하는 리스트
    arr_min_sum(N, 0, 0, used)          # min_sum을 조작하는 함수 사용
    print(f'#{tc} {min_sum}')
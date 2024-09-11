import sys
sys.stdin = open("sample_input.txt","r")

def subset_sum_cnt(arr, N, K):
    cnt = 0
    total_subset = 1 << N  # 비트마스크로 부분집합 개수(2^N) 생성 # total_subset = 16

    for mask in range(1, total_subset): # 공집합 제외하고 순회시작 (최소 1개 이상의 수를 선택이니까..)
        subset_sum = 0
        for i in range(N):
            if mask & (1 << i): # mask의 i번째 인덱스가 1이면
                subset_sum += arr[i] # arr의 i번째 인덱스 값을 +=1
        if subset_sum == K: # 부분집합의 합이 K라면
            cnt += 1 # 경우의 수 += 1
    return cnt


T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split()) # N : 자연수 갯수 / K : 부분 집합의 합
    arr = list(map(int, input().split())) # arr : N개의 숫자

    result = subset_sum_cnt(arr, N, K)

    print(f'#{t} {result}')

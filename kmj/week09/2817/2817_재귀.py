def subsets_sum(i,N,K):
    global cnt
    sub_sum = 0
    # 기저조건
    if i == N : # 부분집합이 만들어졌으므로 합구하기
        for j in range(N):
            if a[j] :
                sub_sum += arr[j]
        if sub_sum == K: # 부분집합의 합이 K면 += cnt
            cnt += 1

    else:
        a[i] = 1
        subsets_sum(i+1,N,K)
        a[i] = 0
        subsets_sum(i+1,N,K)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())  # N : 자연수 / K : 부분집합의 합
    arr = list(map(int, input().split()))

    a = [0] * (N+1)
    cnt = 0 # 부분집합의 합이 K인 갯수 (최종)

    subsets_sum(0,N,K)
    print(f"#{tc} {cnt}")
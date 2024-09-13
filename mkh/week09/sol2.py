for t in range(int(input())) :
     
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
     
    cnt = 0
    for i in range(1<<N) :
        hap = 0
        for j in range(N) :
            if i & (1 << j) : hap += li[j]
            if hap > M: break
        if hap == M : cnt += 1
     
    print(f"#{t + 1} {cnt}")
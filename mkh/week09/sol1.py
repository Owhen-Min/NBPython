def partial_sum(sum=0, idx=0):
    if sum > K:
        return
    # 현재까지의 합이 목표 점수를 넘으면, 멈춘다
    elif sum == K:
        global cnt
        cnt += 1
        return
    # 현재까지의 합이 목표 점수라면, cnt에 더하고 끝낸다.
    elif idx == N:
        return
    # 현재까지의 합이 목표 점수보다 작으면, 마지막에 더했던 숫자 다음 숫자를 넣은 값과 안 넣은 값을 넣어서 돌린다.
    else:
        partial_sum(sum + numbers[idx],idx+1)
        partial_sum(sum, idx+1)
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    numbers = list(map(int,input().split()))
    cnt = 0
    partial_sum()
    print(f'#{tc} {cnt}')
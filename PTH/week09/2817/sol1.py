import sys
sys.stdin = open('input.txt', 'r')
'''
1
4 3
1 2 1 2

'''
# N개의 원소를 갖는 집합의 부분집합 중에, 합이 M인 부분집합의 갯수
def subset(start_idx=0, current_subset=[], total=0):
    global cnt
    # 종료 조건
    # 1. total sum 이 M 이거나 M 을 넘어버릴 때 => 백트래킹
    # 2. 끝까지 돌았을 때
    if total > M:
        return
    if total == M:
        cnt += 1
        return
    if start_idx == N:
        return

    # 현재 원소가 포함되지 않는 경우
    subset(start_idx+1, current_subset, total)
    # 현재 원소가 포함 된 경우
    current_subset.append(arr[start_idx])
    subset(start_idx+1, current_subset, total+arr[start_idx])
    current_subset.pop()

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    # print(N)
    # print(M)
    # print(arr)
    cnt = 0
    subset()
    print(f'#{tc} {cnt}')

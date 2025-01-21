from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

# 1. 큐(데크) 초기화: 1부터 n까지
dq = deque(range(1, n+1))

ans = 0  # 2번, 3번 연산 횟수 누적

for t in targets:
    # 2. 현재 데크에서 t 값의 인덱스를 찾는다
    idx = dq.index(t)  # t가 dq의 몇 번째 위치에 있는지

    # 3. 왼쪽으로 이동/오른쪽으로 이동 중 더 가까운 쪽으로 회전
    #    (len(dq) // 2를 기준으로 왼쪽/오른쪽 어느 쪽이 이득인지 확인)
    if idx <= len(dq) // 2:
        # 왼쪽 회전(연산 2) idx번
        dq.rotate(-idx)  # rotate에 음수를 넣으면 왼쪽으로 회전
        ans += idx
    else:
        # 오른쪽 회전(연산 3) (len(dq) - idx)번
        dq.rotate(len(dq) - idx)  # 양수를 넣으면 오른쪽으로 회전
        ans += (len(dq) - idx)

    # 4. 이제 맨 앞(왼쪽)에 온 t를 빼낸다 (연산 1)
    dq.popleft()

# 결과 출력
print(ans)
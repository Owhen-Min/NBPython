# 찾아야하는 요소의 현재 인덱스 위치를 찾아서(.index()) 최소로 회전할 수 있는 거리를 찾아야겠구나

N, M = map(int, input().split())
target = list(map(int, input().split()))

q = list(range(1,N+1)) # [1,2,3,4,5,6,7,8,9,10]
result = 0

for t in  target:
    # 타겟 인덱스 찾기
    idx = q.index(t)

    # 어느 방향으로 회전해야 횟수가 젤 작을까요~?
    left = idx
    right = len(q)-idx

    # 회전 시작
    if left <= right:  # 왼쪽 회전
        q = q[left:] + q[:left]
    else:  # 오른쪽 회전
        q = q[-right:] + q[:-right]

    result += min(left, right)  # 회전 횟수 카운트
    q.pop(0) # 타겟 삭제

print(result)

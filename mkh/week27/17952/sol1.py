# 문제: 과제는 즉시 시작해야 하며, 매 분마다 새로운 과제가 올 수도 있다.
# 과제를 받으면 남은 시간 안에 해결해야 점수를 얻을 수 있다.
# 뒤에서부터 과제 수행 가능 여부를 판단하여 총 점수를 계산하는 문제.

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 총 시간(분) n
stack = deque()   # (시간, (점수, 소요시간))을 저장할 스택
ans = 0           # 최종 점수 합계

# 과제 입력 처리
for i in range(n):
    index, *info = map(int, input().split())
    if info:
        # 과제가 주어진 경우만 스택에 저장
        # info = [점수, 소요시간]
        stack.append((i, info))

last = n  # 현재 남은 시간 (맨 끝부터 시작)

# 뒤에서부터 과제를 수행할 수 있는지 확인
while stack:
    assigned_time, (score, required_time) = stack.pop()  # 과제 꺼내기
    # 만약 과제를 끝낼 충분한 시간이 남았다면
    if last >= required_time + assigned_time:
        ans += score   # 점수 획득
        last -= required_time # 남은 시간 감소
    else:
        # 과제를 완료할 수 없다면 남은 시간을 현재 시간으로 갱신
        # (지금 과제를 포기하고 그 전 시간대 과제 검토)
        last = assigned_time

print(ans)  # 최종 점수 출력
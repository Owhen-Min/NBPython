import sys
input = sys.stdin.readline

n = int(input())
stack = []  # 현재 하고 있는 과제만 관리
ans = 0     # 최종 점수
pointer = -1

for _ in range(n):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        score, time = query[1], query[2]
        stack.append([score, time])  # 새로운 과제를 시작
        pointer += 1
    if stack:
        # 지금 하고 있는 과제 진행 (1분 소요)
        stack[pointer][1] -= 1
        if stack[pointer][1] == 0:
            # 과제 완료
            ans += stack[pointer][0]
            stack.pop()
            pointer -= 1

print(ans)

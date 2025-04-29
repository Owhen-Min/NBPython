import sys
input = sys.stdin.readline

n = int(input())
stack = []  # 현재 하고 있는 과제만 관리
ans = 0     # 최종 점수

for _ in range(n):
    query = input().split()
    
    if query[0] == "1":
        score, time = int(query[1]), int(query[2])
        if time == 1:
            ans += score
        else:
            stack.append([score, time-1])  # 새로운 과제를 시작
    else:
        if stack:
            stack[-1][1] -= 1
            if not stack[-1][1]:
                ans += stack.pop()[0]

print(ans)

# 과제하는 방식이 스택

N = int(input()) # 이번 학기 시간
score = 0  # 최종 결과 (이번학기에 받을 수 있는 총점)
stack = []

# 이번 학기 시간동안 반복
for i in range(1, N+1):
    info = list(map(int, input().split()))

    # 과제 생김 (1)
    if info[0] == 1:
        a, t = info[1], info[2]  # 점수, 시간
        stack.append([a, t-1])  # 과제를 한 후, 스택넣기
        if stack[-1][1] == 0:   # 과제가 끝났다면
            score += stack.pop()[0]  # 스택에서 제거 + 점수 추가

    else:  # 과제가 없다면(야호!)
        if stack:  # 스택이 비었을 수도 있으므로 체크
            stack[-1][1] -= 1  # 하던 과제를 해야지...(에휴)
            if stack[-1][1] == 0:
                score += stack.pop()[0]

print(score)

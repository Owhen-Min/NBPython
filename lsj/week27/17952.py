N = int(input())
answer = 0
assgin_list = []
score = 0
time = 0
for _ in range(N):
    new = list(map(int, input().split()))
    if new[0] == 1:
        A = new[1] # 과제의 만점
        T = new[2] # 해결하는 데 걸리는 시간
        if time > 0:    # 하고 있는게 있으면
            assgin_list.append((score, time))
        score = A
        time = T
    elif new[0] == 0:
        pass

    if time > 0:
        time -= 1
        if time == 0:
            answer += score
            if assgin_list:
                score, time = assgin_list.pop()

print(answer)

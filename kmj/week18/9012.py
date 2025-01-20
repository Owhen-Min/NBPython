T = int(input())

for _ in range(T):
    strings = input()
    stack=[] # 스택
    flag = True # 플래그

    for s in strings:
        if s == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif s == '(':
            stack.append(s)
        else:
            flag = False # 위의 조건에 부합 x -> not VPS -> 더 이상 볼 가치도 없음
            break

    if not stack and flag: # 스택이 비어있고, 플래그가 T를 유지하고 있다면
        print('YES')
    else:
        print('NO')

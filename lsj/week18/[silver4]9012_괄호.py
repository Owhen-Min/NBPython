T = int(input())

for tc in range(T):
    ls = input()

    # ls의 길이가 홀수라면
    if len(ls) % 2 == 1:
        print("NO")
        continue

    stack = []
    VPS = True

    for str in ls:
        if str == '(':
            stack.append(str)  # 열린 괄호는 스택에 push
        elif str == ')':
            if stack:
                stack.pop()  # 스택에 저장된 열린 괄호가 있으면 pop
            else:
                VPS = False  # 스택이 비어있다면 균형이 맞지 않음
                break

    # 문자열 끝까지 탐색 후 스택에 열린 괄호가 남아 있으면 "NO"
    if VPS and not stack:
        print("YES")
    else:
        print("NO")
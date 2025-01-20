# 시간이 2644mm 걸리는게 맞아,,,?

N = int(input())
cur_num = 1  # 스택에 넣을 숫자
stack = []
result = []  # 수열을 만들기 위한 연산 기록
flog = False

for _ in range(N):
    input_num = int(input())  # 현재 입력된 숫자

    # input_num을 만들기 위해 스택에 숫자를 추가
    while cur_num <= input_num:
        stack.append(cur_num)
        result.append('+')
        cur_num += 1  # 다음에 stack에 넣어야할 숫자 갱신

    # stack에서 input_num을 찾았다!! => pop
    if stack and stack[-1] == input_num:
        stack.pop()
        result.append('-')
    else:
        # 불가능
        flog = True
        print('NO')
        break

if not flog:
    print('\n'.join(result))

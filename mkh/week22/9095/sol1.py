from functools import lru_cache

n = int(input())
ls = [int(input()) for _ in range(n)]

# 함수에 특정 값이 들어갔던 적이 있다면 그 값을 기억해서 예전의 값을 찾아내는 데코레이터. 기본 값으로는 256개의 계산을 모아두고 있는다.
@lru_cache()
def divide(num):
    if num > 3:
        # 숫자가 3이 넘는다면, 앞에 1을 붙이고 나머지를 처리하는 경우, 앞에 2를 붙이고 나머지를 처리하는 경우, 앞에 3을 붙이고 나머지를 처리하는 경우로 나눌 수 있다.
        return divide(num-1) + divide(num-2) + divide(num-3)
    if num == 3:
        # 숫자가 3이라면, 111, 12, 21, 3 4가지의 경우로 표현할 수 있다.
        return 4
    if num == 2:
        # 숫자가 2라면 11, 2 2가지의 경우로 표현할 수 있다.
        return 2
    if num == 1:
        return 1

for num in ls:
    print(divide(num))

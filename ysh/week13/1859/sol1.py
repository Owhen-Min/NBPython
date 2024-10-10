# import sys
# sys.stdin = open('input.txt')

def purchase_plan(price_list):
    stack = price_list[-1] # 현재 최대값
    max_profit = 0 # 얻은 최대 이윤
    for i in range(n - 2, -1, -1): # 역순으로 비교
        stack = max(stack, price_list[i]) # 해당 날짜 매매가와 비교
        max_profit += stack - price_list[i] # 가산

    return max_profit

def purchase_plan2(price_list):
    stack = price_list[-1]
    max_profit = 0
    for i in price_list[::-1]:
        stack = max(stack, i)
        max_profit += stack - i

    return max_profit

t = int(input()) # 테스트케이스 개수
for test_case in range(1, t + 1): # 시작
    n = int(input()) # 알고있는 날짜수
    days = list(map(int, input().split())) # 매매가 리스트
    result = purchase_plan(days) # 해당 날에 산걸 얼마에 팔면 되는가?
    print(f"#{test_case} {result}")
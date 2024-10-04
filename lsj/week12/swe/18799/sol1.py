from itertools import combinations
 
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    temp = []
    for i in range(1, n+1):
        temp += list(combinations(arr,i))
 
    ls = [num for comb in temp for num in comb] # temp 안의 튜플에 있는 숫자들을 ls 라는 하나의 리스트에 담는 과정
    result = sum(ls)/len(ls)
 
    if result.is_integer():
        print(f'#{tc} {int(result)}')
    else:
        print(f'#{tc} {result}')
def recursion(count, point, calorie):
    global fav
 
    # 종료 조건
    if calorie >= L: # 제한 칼로리에 도달하면
        fav = max(fav, point)   # 최댓값 비교
        return
 
    if count == N:  # 재료를 다 사용하면
        fav = max(fav, point)   # 최댓값 비교
        return
 
 
    if calorie + calorie_ls[count] <= L:
        recursion(count+1, point+point_ls[count], calorie+calorie_ls[count])    # 제한 칼로리 넘지 않으면 현재 재료 선택
    recursion(count+1, point, calorie)  # 현재 재료 선택하지 않으면 다음 재료 탐색
 
 
 
T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())    # 재료 수 , 제한 칼로리
    point_ls = []   # 재료의 선호도 점수
    calorie_ls = [] # 재료의 칼로리
    fav = 0 # 가장 높은 점수 기록
    for _ in range(N):
        T, K = map(int, input().split())
        point_ls.append(T)
        calorie_ls.append(K)
    recursion(0,0,0)
    print(f'#{tc} {fav}')
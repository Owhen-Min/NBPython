def solution(coin, cards):
    n = len(cards)
    anchor = n//3
    needs = [0]*(n+1)
    # 짝을 만들기 위해 필요한 카드의 인덱스를 담을 needs. 만약 짝이 만들어지는 경우 인덱스를 음수로 담아서 판별
    for i in range(n):
        if not needs[i+1]:
            j = cards.index(n+1-cards[i])
            needs[i+1] = j+1
            needs[j+1] = -i-1
            # [0, 6, 3, -2, 11, 10, -1, 9, 12, -7, -5, -4, -8]
    poss_round = 1      # 정답을 담을 갈 수 있는 라운드
    temp = 0            # 코인을 두 개 써야 갈 수 있는 경우를 담아둘 temp 이거는 최후의 수단이다!
    i = 1               # 카드를 보는 index i
    while i <= anchor + poss_round*2 and i <=n:
        if needs[i] < 0:
            # 필요한 카드와 현재 카드가 다 처음 받는 핸드에 있는 경우 그냥 더 갈 수 있는 라운드 + 1
            if i <= anchor:
                poss_round += 1
            # 처음 받는 핸드 + 코인 써서 고를 수 있는 카드로 짝이 구성되어 있고 코인이 남아 있다면
            # coin -1, 갈 수 있는 라운드 +1 
            elif needs[i] >= -anchor and coin:
                coin -= 1
                poss_round += 1
            # coin이 없거나 두 짝이 모두 코인을 써서 담아야 하는 경우 temp에 +1
            else:
                temp +=1
        i += 1
        # 처음에 들고 있던 카드로는 짝을 만들 수 없는데 갈 수 있는 곳까지 다 간 경우에, 
        # 내가 안 고른 카드 두 개를 고르면 통과시킬 수 있는지 확인한다.
        if i > anchor + poss_round*2 and temp and coin > 1:
            temp -= 1
            coin -= 2
            poss_round += 1

    return poss_round

print(solution(4,[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
print(solution(3,[1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))
print(solution(2,[5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))
print(solution(10,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))

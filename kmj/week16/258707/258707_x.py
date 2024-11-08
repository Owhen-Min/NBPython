## 못 품 

# n+1 수를 최대한 만들기?

def solution(coin, cards):
    n = len(cards)  # 카드 뭉치 길이
    rounds = 0  # 최대 라운드 수
    target = n + 1  # 목표 합
    hand = set(cards[:n // 3])  # 처음에 n/3장의 카드를 집합으로 초기화
    index = n // 3  # 카드 뽑기 시작 인덱스

    # 카드뭉치(cards)가 모두 소진될 때까지 반복
    while index < n - 1:
        # 새로 뽑은 카드 2개
        hand1, hand2 = cards[index], cards[index + 1]
        pick_trun = {hand1, hand2}  # 새로 뽑은 카드 두 개를 집합으로 저장
        index += 2  # 카드 두 개를 뽑았으므로 인덱스 이동

        # 1. 현재 손에 있는 카드로 n+1 만들기
        pair_found = False
        for num in list(hand):
            t = target - num
            if t in hand:
                # n+1 조합을 찾으면 손에 있는 카드 두 장을 사용해 라운드를 진행
                hand.remove(num)
                hand.remove(t)
                rounds += 1
                pair_found = True
                break

        if pair_found:
            continue

        # 2. 뽑은 카드로 n+1 만들 수 있나? (동전 1개 소모)
        if coin >= 1:
            for num in list(hand):
                t = target - num
                if t in pick_trun:
                    # 동전 1개를 소모하여 새로 뽑은 카드 중 하나와 손에 있는 카드로 조합
                    hand.remove(num)
                    pick_trun.remove(t)
                    rounds += 1
                    coin -= 1
                    pair_found = True
                    break

        if pair_found:
            continue

        # 3. 새로 뽑은 카드 두 장 모두를 사용해 n+1 만들기 (동전 2개 소모)
        if coin >= 2:
            for num in list(pick_trun):
                t = target - num
                if t in pick_trun and num != t:
                    pick_trun.remove(t)
                    pick_trun.remove(num)
                    rounds += 1
                    coin -= 2
                    pair_found = True
                    break
        
        # 4. 조합을 만드는데 실패했다? 게임 끝
        if not pair_found:
            break

        # 새로운 카드들을 손에 추가
        hand.update(pick_trun)

    return rounds

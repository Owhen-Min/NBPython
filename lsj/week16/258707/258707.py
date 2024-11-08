from itertools import combinations

def check_combination(check_arr, card_sum): # 조합 내 조건을 만족하는 카드 있는지 체크하는 함수
    for a, b in combinations(check_arr, 2):
        if a + b == card_sum:
            return True, (a, b)
    return False, None

def solution(coin, cards):
    n = len(cards)
    card_sum = n + 1  # 목표 카드 합 (n + 1)
    check_arr = cards[:n // 3]   # 초기 카드 n/3 장을 가짐
    answer = 1 # 1라운드부터 시작
    card_index = n // 3  # 다음으로 뽑을 카드의 시작 인덱스
    coin_count = coin  # 남은 동전 수

    # 게임 진행


 # 처음 내가 가지고 있었던 카드에서 조건을 만족하는 카드가 있는지 확인
    has_combination, combination = check_combination(check_arr, card_sum)

    if has_combination:  # 조건을 만족하는 카드가 있다면
        a, b = combination
        check_arr.remove(a)
        check_arr.remove(b)
        answer += 1  # 바로 다음 라운드로

    while coin_count >= 0 and card_index + 1 < n:  # 카드가 2장 이상 남아있고 동전이 있을 때만

        # 카드 두 장 먼저 뽑고 시작
        new_card1 = cards[card_index]
        new_card2 = cards[card_index + 1]
        check_arr.append(new_card1)
        check_arr.append(new_card2)

        card_index += 2

        # 1. 손에 있는 카드에서 조건을 만족하는 조합이 있는지 확인
        has_combination, combination = check_combination(check_arr, card_sum)

        if has_combination:
            # 조건을 만족하면 두 카드를 a, b
            a, b = combination

            # 조건을 만족하는 두 카드가 새로 뽑은 카드라면

            if new_card1 in (a, b):
                coin_count -= 1
                check_arr.remove(new_card1)

            if new_card2 in (a, b):
                coin_count -= 1
                check_arr.remove(new_card2)

            if coin_count < 0:
                return answer # 다음 라운드 진출 불가

            else: # 코인이 남아 있다면
                if a in check_arr:
                    check_arr.remove(a)
                if b in check_arr:
                    check_arr.remove(b)
            answer += 1

        else:
            return answer
    return answer

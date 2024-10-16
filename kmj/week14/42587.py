from collections import defaultdict

def solution(clothes):
    # 기본값이 0인 defaultdict 생성
    clothes_cnt = defaultdict(int) # defaultdict(<class 'int'>, {})

    # 의상 목록을 카테고리별로 세기
    for _, category in clothes:
        clothes_cnt[category] += 1 # {'headgear': 2, 'eyewear': 1}

    # 조합
    answer = 1
    for i in clothes_cnt.values(): # dict_values([2, 1])
        answer *= i+1 # 하나의 의상 종류에서 선택을 안하는 경우도 포함

    return answer -1 # 모든 의상을 선택 안한 경우 뺴주기
    

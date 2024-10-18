def solution(clothes):
    # 카테고리별 개수를 저장할 딕셔너리 생성
    category_dict = {}

    # 카테고리별로 옷의 개수 카운트
    for cloth, category in clothes:
        if category in category_dict:
            category_dict[category] += 1  # 이미 키가 있으면 +1
        else:
            category_dict[category] = 1   # 키가 없으면 1로 초기화

    # 각 종류의 (옷 개수 + 1)을 곱한 후, 아무것도 안 입는 경우 1가지 빼기
    result = 1
    for value in category_dict.values():
        result *= (value + 1)  # 해당 카테고리의 옷을 입지 않는 경우를 포함

    # 아무것도 입지 않는 경우(1가지) 제외
    return result - 1
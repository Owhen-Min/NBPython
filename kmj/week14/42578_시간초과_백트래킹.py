# 내 코드 아님
# 백트래킹을 사용하면 어떨까 생각했는데 구현해보니 시간초과

def solution(clothes):
    # 의상 종류별로 분류하기 위한 딕셔너리 생성
    clothes_dict = {}

    # 의상 목록을 딕셔너리에 추가
    for name, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = []
        clothes_dict[category].append(name)

    # 백트래킹 함수 정의
    def backtrack(selected, categories):
        # 모든 카테고리를 다 선택했으면
        if not categories:
            return 1 if selected else 0  # 최소 1개의 의상 선택 시 1 반환, 아니면 0 반환

        # 현재 카테고리에서 의상 선택
        current_category = categories[0]
        count = 0

        # 의상을 선택하는 경우
        for item in clothes_dict[current_category]:
            count += backtrack(selected + [item], categories[1:])

        # 의상을 선택하지 않는 경우
        count += backtrack(selected, categories[1:])

        return count

    # 카테고리 목록을 가져와서 백트래킹 시작
    category_list = list(clothes_dict.keys())
    answer = backtrack([], category_list)

    return answer

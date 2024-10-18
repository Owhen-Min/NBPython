from collections import defaultdict


def solution(clothes):
    types = defaultdict(int)
    # 옷의 종류들을 키값으로, 개수를 value로 갖는 딕셔너리를 생성한다.
    for _, t in clothes:
        types[t] += 1

    answer = 1
    # 부분집합의 개수는 각 요소들이 들어가지 않는다, 아이템이 들어간다의 경우의 수로
    # 딕셔너리의 value+1을 각각 answer에 곱해주면 부분집합의 수를 구할 수 있다.
    for count in types.values():
        answer *= (count+1)

    # 모두 들어가지 않은 경우는 문제에서 숫자로 세지 않으므로 1을 차감한 값을 반환한다.
    return answer-1
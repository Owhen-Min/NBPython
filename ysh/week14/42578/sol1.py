### 코디하는 방법의 총수?
# 부위별 의상의 수 + 1한 값을 모두 다 곱하고 -1 한다.
### why?
# 만약에 빨간 모자, 파란 모자 이렇게 2개의 머리부분 의상이 있다면?
# 안쓴다 1가지, 빨간 모자를 쓴다 1가지, 파란 모자를 쓴다 1가지로
# 경우의 수는 총 3가지가 되기 때문에 +1을 한다.
### 그럼 왜 -1을 해야하는 가?
# 모든 부위에서 안입는다를 골라버리는 경우는 제외 해야하기 때문
### 해결방법?
# 그러면 우리의 목표는 의상의 부위별 개수만 헤아리면 된다.
# 문제에서 중복되는 옷은 없다고 했기 때문에 카운트 하기 편해진다.

def solution(clothes):
    answer = 1
    costumes = dict()
    for name, cloth_type in clothes:
        if cloth_type in costumes.keys():
            costumes[cloth_type] += 1
        else:
            costumes[cloth_type] = 1
    for cnt in costumes.values():
        answer *= cnt + 1
    return answer - 1
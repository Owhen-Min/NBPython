'''
경우의 수 구하기
- 우리는 같은 종류의 옷들중에 한가지만 입을 수 있다.
- 아예 안입는건 안된다.
- 즉, 예를 들어 상의,하의 두가지 종류의 옷이 있다면 그 경우의 수는 = {(상의갯수 + 1) * (하의갯수 + 1)...} - 1
(여기서 -1 은 아무것도 입지 않았을 경우. 그 경우는 불가능하므로 -1 해준다.)
'''

def solution(clothes):
    # 의상이름 : 의상종류 => 형태로 담을 딕셔너리 dict 를 만든다
    dict = {}
    # 입력받은 clothes 안에 있는 각각의 cloth 를 하나씩 확인하며
    # dict 안에 같은 종류의 cloth 가 있는지 확인한다.
    for cloth in clothes:
        name, kind = cloth
        # 확인 후, 같은 종류의 cloth 가 있으면 +1 해주고, 없다면 해당 항목을 생성한다.
        if kind in dict:
            dict[kind] += 1
        else:
            dict[kind] = 1

    # 각 의상 종류의 선택할 수 있는 경우의 수 계산
    # (의상 개수 + 1)로 계산하여 선택하지 않는 경우도 포함
    result = 1
    for count in dict.values():
        result *= (count + 1)

    # 최소 하나의 의상은 입어야 하므로 1을 빼줌
    return result - 1

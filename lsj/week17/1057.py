def find_round(N, JM, HS):
    count = 0

    # 두 사람이 같은 그룹에 속할 때까지 반복
    while JM != HS:
        # 번호 업데이트
        JM = abs((JM + 1) // 2)
        HS = abs((HS + 1) // 2)
        count += 1

    return count

N, JM, HS = map(int, input().split())
print(find_round(N, JM, HS))

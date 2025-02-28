text = input()
if not text or text[0] == '0':
    print(0)

else:
    prev, curr = 1, 1  # 초기값: i=-1과 i=0에 해당
    MOD = 1000000

    for i in range(1, len(text)):
        temp = 0
        if text[i] != '0':
            temp = curr  # 단일 숫자로 해석 가능
        if 10 <= int(text[i-1:i+1]) <= 26:
            temp += prev  # 두 자리 숫자로 해석 가능
        temp %= MOD
        prev, curr = curr, temp

    print(curr)

# 4 6
# a t c i s w

# l, c가 들어오는데 c개의 글자 중에서 l개를 골라서 만들 수 있는 글자수 조합 구하기. c개의 글자는 다음 줄에 들어온다.
# 단 1. 정렬이 되어있어야 하며, 2. 1개 이상의 모음과 2개 이상의 자음이 있어야 함.
# 모음의 개수가 5개로 압도적으로 적으므로, 모음의 수로 체크하는게 편하다.

l, c = map(int,input().split())
ls = sorted(input().split())

vowels = {'a', 'e', 'i', 'o', 'u'}

def dfs(depth, string):
    if len(string) == l:
        consonant = 0
        vowel = 0
        for char in string:
            if char in vowels:
                vowel += 1
            else:
                consonant += 1
        if vowel > 0 and consonant > 1:
            print(string)
            return
    else:
        try:
            dfs(depth+1, string+ls[depth])
            dfs(depth+1, string)
        except:
            pass

dfs(0, '')
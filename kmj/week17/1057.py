# next_round을 매 라운드마다 만들어서 kim과 im이 만날 때까지 반복
N, kim, im = map(int, input().split())

game = [i + 1 for i in range(N)]  # [1, 2, 3, ..., N]
round = 0
found = False  # kim, im은 만났는가??

while len(game) > 1:
    round += 1
    next_round = []
    
    for i in range(0, len(game), 2):
        # 마지막 인덱스가 혼자 남은 경우 (홀수)
        if i + 1 >= len(game):
            next_round.append(game[i])
            continue

        # 두 사람이 같은 라운드에서 만나면 종료
        if (game[i] == kim and game[i + 1] == im) or (game[i] == im and game[i + 1] == kim):
            found = True
            break
        # 승자는 다음 라운드로
        # kim,im 우선 > 인덱스 빠른자 우선
        if game[i] == kim or game[i + 1] == kim:
            next_round.append(kim)
        elif game[i] == im or game[i + 1] == im:
            next_round.append(im)
        else:
            next_round.append(game[i])

    # 두 사람이 만났다면 종료
    if found:
        break

    # 다음 라운드 준비
    game = next_round

print(round)

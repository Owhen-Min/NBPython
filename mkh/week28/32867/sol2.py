import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = -1
min_note = max_note = -1000

for note in map(int, input().split()):
    if note > max_note:
        max_note = note
    elif note < min_note:
        min_note = note
    else: continue

    if max_note - min_note >= k:
        ans += 1
        min_note = max_note = note

print(ans)
n, k = map(int,input().split())
notes = tuple(map(int,input().split()))
ans = 0

min_note=max_note=notes[0]
spare = k-1

for note in notes:
    if note < min_note-spare or note > max_note + spare:
        min_note=max_note=note
        spare = k-1
        ans += 1
    else:
        if note < min_note:
            spare -= min_note - note
            min_note = note
        elif note > max_note:
            spare -= note - max_note
            max_note = note

print(ans)
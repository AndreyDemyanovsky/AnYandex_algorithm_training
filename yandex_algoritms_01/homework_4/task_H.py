from string import ascii_letters

len_w, len_s = map(int, input().split())

w = input()
text = input()

letters_w = {i: 0 for i in w}
letters_s = {i: 0 for i in ascii_letters}
for i in range(len_w):
    letters_w[w[i]] += 1
    letters_s[text[i]] += 1


def match_dicts(sequenc1, sequenc2):
    match_ = 0
    for i in sequenc1:
        if sequenc1[i] == sequenc2.get(i, None):
            match_ += 1
    return match_


match_ = match_dicts(letters_w, letters_s)
l = 0
result = 1 if match_ == len(letters_w) else 0

for i in range(len_w, len_s):
    fl = text[i]
    ll = text[l]

    if ll in letters_w and letters_s[ll] == letters_w[ll]:
        match_ -= 1
    letters_s[ll] -= 1
    if ll in letters_w and letters_s[ll] == letters_w[ll]:
        match_ += 1

    if fl in letters_w and letters_s[fl] == letters_w[fl]:
        match_ -= 1
    letters_s[fl] += 1
    if fl in letters_w and letters_s[fl] == letters_w[fl]:
        match_ += 1

    if match_ == len(letters_w):
        result += 1
    l += 1

print(result)

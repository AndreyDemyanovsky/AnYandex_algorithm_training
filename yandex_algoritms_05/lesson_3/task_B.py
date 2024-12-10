def add_letter(let, dct):
    if let in dct:
        dct[let] += 1
    else:
        dct[let] = 1
    return dct


word_1 = input()
word_2 = input()
ans = "YES"
if len(word_2) == len(word_1):
    dct_let_1 = {}
    dct_let_2 = {}
    for i in range(len(word_1)):
        dct_let_1 = add_letter(word_1[i], dct_let_1)
        dct_let_2 = add_letter(word_2[i], dct_let_2)

    for letter in dct_let_1:
        if letter not in dct_let_2 or dct_let_1[letter] != dct_let_2[letter]:
            ans = "NO"
            break
else:
    ans = "NO"

print(ans)
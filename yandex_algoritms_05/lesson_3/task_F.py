dictionary = {}
for word in input().split():
    first_letter = word[0]

    l = dictionary.setdefault(first_letter, [])
    l.append(word)

res = []
for i in dictionary:
    l = dictionary[i]
    dictionary[i] = sorted(l, key=lambda x:len(x))

for word in input().split():
    output = word
    if word[0] in dictionary:
        for i in dictionary[word[0]]:
            len_w = len(i)
            if len_w < len(output) and i == word[:len_w]:
                output = i
                break
    res.append(output)

print(*res)
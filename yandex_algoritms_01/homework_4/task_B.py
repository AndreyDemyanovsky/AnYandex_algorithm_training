f = open("input.txt", "r")

dict_number_words = {}
lst = []
for line in f.readlines():
    for word in line.split():
        if word not in dict_number_words:
            dict_number_words[word] = 0
            lst.append(0)
        else:
            dict_number_words[word] += 1
            lst.append(dict_number_words[word])

print(*lst)
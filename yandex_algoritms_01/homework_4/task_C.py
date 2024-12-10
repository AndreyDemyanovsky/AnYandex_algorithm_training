import sys

count = 0 
result = None
dct = {}
for line in sys.stdin:
    for word in line.split():

        if word not in dct:
            dct[word] = 1
        else:
            dct[word] += 1

        if dct[word] > count:
             result = word
             count = dct[word]

        elif dct[word] == count and word < result:
            result = word

print(result)

# words = {}
# word_count = {1: []}

# for line in sys.stdin:
#     for word in line.split():
#         if word not in words:
#             words[word] = 1
#             word_count[1].append(word)
#         else:
#             n  = words[word] + 1
#             words[word] = n
#             word_count.setdefault(n, []).append(word)

# m = max(word_count)
# print(min(word_count[m]))

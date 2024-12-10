N = int(input())
dict_words = {}
for _ in range(N):
    word = input()
    dict_words.setdefault(word.lower(), set()).add(word)

errors = 0
for word in input().split():
    is_errors = True
    low_word = word.lower()
    if low_word in dict_words:
        if word in dict_words[low_word]:
            is_errors = False
    else:
        counter = [1 for i in word if i.isupper()]
        if len(counter) == 1:
            is_errors = False

    if is_errors:
        errors += 1

print(errors)

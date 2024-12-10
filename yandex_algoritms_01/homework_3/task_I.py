count_schoolchildren = int(input())

languages_everyone_knows = set()
languages_least_one_knows = set()
flag = True
for _ in range(count_schoolchildren):

    n = int(input())
    languages = set([input() for _ in range(n)])
    languages_least_one_knows.update(languages)

    if flag:
        languages_everyone_knows.update(languages_least_one_knows)
        flag = False
    else:
        languages_everyone_knows = languages_everyone_knows.intersection(languages)


print(len(languages_everyone_knows))
print(*languages_everyone_knows, sep="\n")

print(len(languages_least_one_knows))
print(*languages_least_one_knows, sep="\n")


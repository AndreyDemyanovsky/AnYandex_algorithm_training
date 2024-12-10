N = int(input())
dict_words = {}
for _ in range(N):
    s, s1 = input().split()
    dict_words[s1] = s
    dict_words[s] = s1

word = input()
print(dict_words[word])
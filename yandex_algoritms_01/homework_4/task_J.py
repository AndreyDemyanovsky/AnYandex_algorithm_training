import sys
from string import ascii_letters, digits

ascii_letters += digits + "_"


def data_processing(n):
    if n.isdigit():
        return int(n)
    return True if n == "yes" else False


def maybe_identifier(s):
    if s in key_words or s.isdigit():
        return False

    if s[0].isdigit():
        if len(s) == 1 or not start_digit:
            return False
    return True


def cleaning_row(s):
    clear_string = "".join([letter if letter in ascii_letters else " " for letter in s])
    return clear_string.split()


count_key_words, case_sensitive, start_digit = map(data_processing, input().split())
key_words = set()
for _ in range(count_key_words):
    kw = input()
    if not case_sensitive:
        key_words.add(kw.lower())
    key_words.add(kw)

identifiers = {}
position = 1
for row in sys.stdin:
    if not case_sensitive:
        row = row.lower()
    for word in cleaning_row(row):
        if maybe_identifier(word):
            if word not in identifiers:
                identifiers[word] = [0, position]
                position += 1
            identifiers[word][0] += 1

result = None
for i in identifiers:
    if not result:
        result = i
    if identifiers[i][0] > identifiers[result][0]:
        result = i
    if identifiers[i][0] == identifiers[result][0] and identifiers[i][1] < identifiers[result][1]:
        result = i

print(result)



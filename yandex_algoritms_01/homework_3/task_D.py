import sys

words = set()
for line in sys.stdin.readlines():
    words.update(line.split())

print(len(words))
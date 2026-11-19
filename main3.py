n = int(input())

synonyms = {}

for i in range(n):
    a, b = input().split()
    synonyms[a] = b
    synonyms[b] = a

word = input()

print(synonyms[word])

words = input().split(',')

unique_words = sorted(set(words))

print(','.join(unique_words))

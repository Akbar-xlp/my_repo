words = map(str, input().split())

lower_words = [word.lower() for word in words]

qnique_words = set(lower_words)

print(len(qnique_words))

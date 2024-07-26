def gen(text):
    for word in text:
        yield word.upper()


a = gen(["apple","banana", "cherry"])
try:
    print(next(a))
    print(next(a))
    print(next(a))
except StopIteration:
    print("Stop Interpretation")
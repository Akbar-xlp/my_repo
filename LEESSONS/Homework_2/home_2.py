text = input()
digits_set = set()
for letter in text:
    if letter.isdigit():
        digits_set.add(letter)
for digit in digits_set:
    print(digit,end=" ")
print()            

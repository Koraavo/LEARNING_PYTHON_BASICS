num = [1, 2, 3, 4, 5]

for item in num:
    if item == 3:
        print("Found!")
        break
    print(item)


for item in num:
    if item == 3:
        print("Found!")
        continue
    print(item)

for item in num:
    for letter in 'abc':
        print(item, letter)

'iterates on an iterable'
print("Q1: Names >4 and < 7 characters:")
def challenge(names):
    for name in names:
        if 4 < len(name) < 7:
            print(name)


print("Q2: Sorted names > 7 characters:")
names.sort()
for name in names:
    if len(name) > 7:
        print(name)

print("Q3: Palindromic Names:")
for name in names:
    if name == name[::-1]:
        print(name)

majina = ["Tracy", "Dad", "Moses", "Mom", "Victor", "Tacocat", "Christian"]
challenge(majina)

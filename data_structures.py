# 1. TUPLES
cars = ("Discovery IV", "Mazda CX5", "Nissan GTR", 3.142857)
print(cars)
print(cars[1:4])
print(cars[3])
for xl in cars:
    print(xl)

# 2. LISTS
colours = ["Red", "Orange", "Yellow", "Blue", "Green", "Indigo", "Violet"]
print(colours)

colours[0] = "Crimson"
print(colours)

for y in colours:
    print(y)

colours.reverse()
print(colours)

colours.pop(3)
print(colours)

colours.sort()
print(colours)

colours.sort(reverse=True)
print(colours)

# 3. DICTIONARIES
students = {"ADM1": "JESSE", "ADM2": "WALTER", "ADM3": "TUCO", "ADM4": "SKYLER"}
print(students["ADM2"])
for key1 in students.keys():
    print(key1)
for key2 in students.values():
    print(key2)

# 4. SETS
ranks = {1, 5, 8, 4, 0, 5, 3, 2, 1, 6, 8, 10, 11, 12, 10}
print(ranks)

# ASSIGNMENT
animals = ["Lion", "Zebra", "Giraffe", "Hippopotamus", "Cheetah", "Dog"]
genList = []
for x in animals:
    if len(x) > 5:
        genList.append(x)

for y in genList:
    print(y)

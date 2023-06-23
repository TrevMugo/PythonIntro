def filtered_List(main):
    newList = []
    for x in main:
        if 4 < len(x) < 7:
            newList.append(x)
    return newList


ListItems = ("Giraffe", "Hippopotamus", "Lion", "Dimethyl-propane", "Rhino",
             "Congratulations", "Buffalo", "Pusillanimous", "Horse", "Ducks")
filtered_List = filtered_List(ListItems)
print(filtered_List)


def filtered_List(main):
    new_List = []
    for x in main:
        if len(x) > 7:
            new_List.append(x)
    return new_List


ListItems = ("Giraffe", "Hippopotamus", "Lion", "Dimethyl-propane", "Rhino",
             "Congratulations", "Buffalo", "Pusillanimous", "Horse", "Ducks")
print(filtered_List)

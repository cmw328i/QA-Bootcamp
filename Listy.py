import string


def listy():
    listsize = int(input("How many items would you like to list?\n"))
    i = 0
    list = []

    while i < listsize:
        list.append(input("Enter item to the list\n     "))
        i += 1
    list_b = [x.lower() for x in list]

    element = input(
        "Which element of the list would you like to see the position of?\n     ")
    element = element.lower()
    if element not in list_b:
        print("Oops, that item is not in your list")
    else:
        for index, elem in enumerate(list_b):
            if elem == element:
                print(
                    f"The element {element} occurs in postion {index}")


listy()

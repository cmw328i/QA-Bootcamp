namecount = 0
names = []
while namecount < 5:
    names.append(input("Please enter a name "))
    namecount += 1

count = 0
while count < len(names):
    print(names[count], "is awesome!")
    count += 1

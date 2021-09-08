
name = (input("Enter student's name\n"))
homework = int(input("\nEnter homework grade from 0 to 25\n"))
assessment = int(input("\nEnter assessment grade from 0 to 50\n"))
exam = int(input("\nEnter exam grade from 0 to 100\n"))
result = round(((homework+assessment+exam)/175)*100)
if 90 <= result:
    letter = "A"
elif 80 <= result < 90:
    letter = "B"
elif 70 <= result < 80:
    letter = "C"
elif 60 <= result < 70:
    letter = "D"
else:
    letter = "Fail"

if letter == "A":
    print(f"{name}'s final ICT grade is {result}%\nWhich is an {letter} grade\n\n")
else:
    print(f"{name}'s final ICT grade is {result}%\nWhich is a {letter} grade\n\n")

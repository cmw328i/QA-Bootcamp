import dice


def dice_roll():
    i = 0
    rolls = []
    while i < 2:
        rolls.append(dice.roll())
        i += 1
    print(f"The first die is {rolls[0]}\n\nThe second die is {rolls[1]}\n")


start = input("Press enter to roll the dice!\n")

if start == "":
    dice_roll()
else:
    print("I told you to press enter, you idiot!")

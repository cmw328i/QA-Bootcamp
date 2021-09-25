import math
import string
more = "y"
while more == "y":
    try:
        velocity = float(
            input("\nPlease enter velocity in metres per second\n\n"))/299792458
    except ValueError:
        print("You must enter a valid number between 0 and 299792458")
    if velocity < 0 or velocity > 299792458:
        print("Speed must be between 0 and 299792458")
    else:
        time = math.sin(math.acos(velocity))
        space = 1-time
        print(
            f"\n{space*100}% of your motion is through space.\n\n{time*100}% of your motion is through time.\n")

        more = (input(
            "\n\nEnter y if you would like to try another. Otherwise, press enter to quit: \n\n"))
        more = more.lower()
        if more != "y":
            pass

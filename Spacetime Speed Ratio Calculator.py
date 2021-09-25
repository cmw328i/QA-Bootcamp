import math
velocity = float(
    input("Please enter velocity in metres per second\n\n"))/299792458
if velocity < 0 or velocity > 299792458:
    print("Speed must be between 0 and 299792458")
else:
    time = math.sin(math.acos(velocity))
    space = 1-time

    print(f"\n{space*100}% of your motion is through space.\n\n{time*100}% of your motion is through time.\n")

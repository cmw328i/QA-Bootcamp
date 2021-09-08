hours = input(
    "How many hours do you spend on your phone?\nUse hh:mm format\n").split(":")
time = (int(hours[1]))+(60*int(hours[0]))
fraction = 100*(time/(24*60))
print("you are spending about " + str(round(fraction)) +
      "% of your day on your phone")

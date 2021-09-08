import string
firstname = str(input("Please enter first name\n "))
lastname = str(input("Please enter last name\n "))
fullname = string.capwords(firstname+" "+lastname)
number = str(input("Please enter your house number\n"))
street = str(input("Please enter your street name\n"))
firstline = string.capwords(number+" "+street)
city = string.capwords(input("Please enter your city\n"))
postcode = str(input("Please enter your postcode\n"))
postcode1 = str(postcode.upper())
print("Hello!\n" + fullname + "\n" +
      firstline + "\n" + city + "\n" + postcode1)

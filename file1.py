
warm = input("is it warm? type yes/no  ")
#converting string to boolean
is_warm = "yes" in warm
temp = int(input("Enter temperature  "))

if temp > 19 and is_warm:
    print("It's warm")
else:
    print("So it's cold")

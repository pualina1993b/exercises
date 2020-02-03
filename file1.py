
warm = input("is it warm? type yes/no  ")
#converting string to boolean
is_warm = "yes" in warm
temp = int(input("Enter temperature  "))

if temp > 19 and is_warm:
    print("It's warm")
else:
    print("So it's cold")

def greet_user(first_name, last_name):
    print(f'Hi!!! {first_name} {last_name} !')


#2 line breaks after function
print("Start")
greet_user(input('type your first name  '), input('type your last name  '))
print("Finish")
import math

def greet_user(first_name, last_name):
    print(f'Hi!!! {first_name} {last_name} !')


def get_greet_user_text(first_name, last_name):
    text = f'Hi!!! {first_name} {last_name} !'
    return text


def countDistance2d(firstPlaceA, firstPlaceB, secondPlaceA, secondPlaceB):
    deltaA = secondPlaceA - firstPlaceA
    deltaB = secondPlaceB - firstPlaceB
    return math.sqrt(math.pow(deltaA, 2) + math.pow(deltaB, 2))


# warm = input("is it warm? type yes/no  ")
# # converting string to boolean
# is_warm = "yes" in warm
# temp = int(input("Enter temperature  "))
#
# if temp > 19 and is_warm:
#     print("It's warm")
# else:
#     print("So it's cold")
#
# # 2 line breaks after function
# print("Start")
# greetText = get_greet_user_text(input('type your first name  '), input('type your last name  '))
# print(greetText)
# print("Finish")

name = countDistance2d(0, 0, 2, 2)
print(name)


data = 0

while data < 10:
    print(f"it's working ->{data}")
    if data == 5:
        break # key word
    data += 1


user_prompt = True
current_year = 2022

while user_prompt:
    birth_year = input("Please Enter Your Birth Year")
    if birth_year.isdigit():
        user_prompt = False
        age = birth_year - current_year
        print(f"Your age is {age}")
    else:
        print("Please Enter Your Age In Digits Only")
        break



# print(f"Your age is {age}")
#
# # calculate their age - year of birth etc.
#
# print("Please Enter Your Birth Year")
# birth_year = input
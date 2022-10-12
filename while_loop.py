#

# data = 0
#
# while data < 10:
#     print(f"it's working ->{data}")
#     if data == 5:
#         break # key word
#     data += 1


user_prompt = True

while user_prompt:
    age = input("Please Enter Your Age")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please Enter Your Age In Digits Only")

print(f"Your age is {age}")

# calculate their age - year of birth etc.
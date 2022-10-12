# Pseudo Coding

# weather = "sunny"
#
# # if it's cold:
# if weather == "cold": # True or False
#     print("wear a jacket") # take jacket
# elif weather == "sunny": # if it's sunny
#     print("let's go to the beach") # go to the beach
# # if it's raining:
# else:
#     print("no match found, better luck next time")

# if it's sunny: boolean value true
#   let's go to the beach
# else or elif

# TASK - age restriction for movie tickets
# create a condition for 18 & above
# 16 & above
# universal
# pg
# 12a
# 15 & above
# if nothing matched inform the user to enter their age again
# user must not be allowed to enter age over 117 years

print("Please Enter Your Age")
age = int(input())

if age >= 18 and age <= 117:
    print("You can watch any movie")
elif age >= 16 and age < 18:
    print("You can only watch 16 and above movies")
elif age >= 12 and age < 16:
    print("You can only watch 12a movies")
elif age >= 8 and age < 12:
    print("You can only watch pg movies")
else:
    print("Sorry, you cannot watch any movies here")
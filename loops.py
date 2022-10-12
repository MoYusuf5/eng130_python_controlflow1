# list_data = [1, 2, 3, 4, 5]
# for number in list_data:
#     if number == 3:
#         print("found 3")
#     elif number > 3:
#         print("you have passed 3")
#     else:
#         print("too soon")

# create a dictionary student_data
# iterate through the dict
# using control flow - if - elif - else and for loop print all the keys
# print all the values
# print key with matching value

student_data = {
    "name" : "Mohamed",
    "stream" : "DevOps",
    "completed_lessons" : 3,
    "completed_lessons_names" : ["lists", "strings", "loops"]
}

for k in student_data.keys():
    print(k)

for v in student_data.values():
    print(v)

for k, v in student_data.items():
    print(k,v)
# Python Control Flow
- Control Flow is the order in which the program's code executes
- `if`
- `elif`
- `else`

```python
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
```

# Loops
- Loop through an iterable object and perform the same action for each entry

### Example:
```python
list_data = [1, 2, 3, 4, 5]
for number in list_data:
    if number == 3:
        print("found 3")
    elif number > 3:
        print("you have passed 3")
    else:
        print("too soon")
```
### Task:
```python
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
```

# While Loops
- A while loop can execute a set of statements as long as a condition is true

### Example
```python
data = 0

while data < 10:
    print(f"it's working ->{data}")
    if data == 5:
        break # key word
    data += 1
```
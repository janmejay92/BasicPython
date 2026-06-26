# Boolean values
is_raining = True
is_sunny = False
print(is_raining)
print(is_sunny)

# Comparison operators
age = 18
print(age >= 18)
print(age < 18)

# Relation operator (example with input commented out)
# age = int(input("Enter your age"))
# father_age = int(input("Enter your father age"))
# print(age != father_age)

# Logical operators
# AND operator
age1 = 18
has_adult = True
print(age1 >= 18 and has_adult)

# OR operator
cash = 0
has_card = True
print(cash > 0 or has_card)

# NOT operator
is_raining = False
print(not is_raining)

# If condition
marks1 = 33
if marks1 > 30:
    print("pass")

    # If-else condition
    marks2 = 45
    if marks2 >= 33:
        print("pass")
    else:
        print("fail")

    # If-elif ladder
    marks3 = 95
    if marks3 > 90:
        print("Grade A+")
    elif marks3 > 85:
        print("Grade A")
    elif marks3 > 80:
        print("Grade B+")
    elif marks3 > 75:
        print("Grade B")
    else:
        print("Just pass")

# Nested if-else
age2 = 21
has_id = True
if age2 >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Entry not allowed")
else:
    print("You are minor")

# Ternary operator examples
age3 = 18
status = "Adult" if age3 >= 18 else "Minor"
print(status)

marks4 = 67
status = "Pass" if marks4 >= 33 else "Fail"
print(status)

marks5 = 90
status = "Grade A+" if marks5 >= 90 else "Grade A"
print(status)

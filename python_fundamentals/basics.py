# 1. Variables and Data Types
name = "Alice"         # str
age = 25               # int
height = 5.7           # float
is_student = True      # bool

# 2. Operators
sum_result = age + 5           # Addition
product = age * 2              # Multiplication
is_adult = age >= 18           # Comparison
logical_and = is_student and (age < 30)  # Logical

# 3. Input and Output
user_input = input("Enter your favorite color: ")
print("You entered:", user_input)

# 4. Conditional Statements (if-else)
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Python does not have a native switch statement, but you can use dictionaries:
def switch_example(day):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(day, "Invalid day")

print(switch_example(3))

# 5. Loops
# For loop
for i in range(5):
    print("For loop iteration:", i)

# While loop
count = 0
while count < 3:
    print("While loop count:", count)
    count += 1

# 6. Functions
def greet(person):
    return f"Hello,
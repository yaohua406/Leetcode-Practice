# Data structures in python


# 1. Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[1])  # Access element

# 2. Tuples
coordinates = (10, 20)
print(coordinates[0])

# 3. Dictionaries
person = {"name": "Bob", "age": 30}
person["city"] = "New York"
print(person["name"])

# 4. Sets
unique_numbers = {1, 2, 3, 2}
unique_numbers.add(4)
print(unique_numbers)

# 5. List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# 6. String Manipulation
text = "Hello, World!"
print(text.lower())
print(text.replace("World", "Python"))

# 7. Built-in Functions and Methods
print(len(fruits))           # Length of list
print(sorted(unique_numbers))# Sort set
print(person.keys())         # Dictionary keys
print(text.split(","))       # Split
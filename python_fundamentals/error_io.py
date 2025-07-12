# 1. Error Handling and Exception Handling

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result is:", result)
finally:
    print("Execution completed.")

# Raise custom exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

# 2. File Handling

# Reading a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, file handling in Python!")

# 3. Working with CSV Files
import csv

# Writing CSV
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
    writer.writerow(["Bob", 30])

# Reading CSV
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# 4. Working with JSON Files
import json

data = {"name": "Alice", "age": 25}
# Writing JSON
with open("data.json", "w") as jsonfile:
    json.dump(data, jsonfile)

# Reading JSON
with open("data.json", "r") as jsonfile:
    loaded_data = json.load(jsonfile)
    print(loaded_data)

# 5. Working with XML Files
import xml.etree.ElementTree as ET

# Creating XML
root = ET.Element("person")
ET.SubElement(root, "name").text = "Alice"
ET.SubElement(root, "age").text = "25"
tree = ET.ElementTree(root)
tree.write("person.xml")

# Reading XML
tree = ET.parse("person.xml")
root = tree.getroot()
for child in root:
    print(child.tag, ":", child.text)
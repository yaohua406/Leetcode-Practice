# 1. Standard Library Modules
import math
import random
import datetime
import os

print(math.sqrt(16))                # Square root
print(random.randint(1, 10))        # Random integer
print(datetime.datetime.now())      # Current date and time
print(os.getcwd())                  # Current working directory

# 2. Creating Your Own Module (save as mymodule.py)
# def greet(name):
#     return f"Hello, {name}!"

# Importing your own module
# import mymodule
# print(mymodule.greet("Alice"))

# 3. Creating a Package
# Directory structure:
# mypackage/
#   __init__.py
#   module1.py
#   module2.py

# Example usage:
# from mypackage import module1
# module1.some_function()

# 4. Installing External Packages (pip)
# Run in terminal:
# pip install requests

import requests
response
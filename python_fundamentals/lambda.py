# 1. Lambda Functions
add = lambda x, y: x + y
print(add(2, 3))

# 2. Map, Filter, and Reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)

print(squared)
print(even)
print(product)

# 3. Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 4. Generators and Iterators
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)

# 5. *args and **kwargs
def demo_args_kwargs(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo_args_kwargs(1, 2, 3, a=4, b=5)

# 6. Context Managers (with statements)
with open("sample.txt", "w") as f:
    f.write("Hello from context manager!")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
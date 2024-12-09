def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(num):
    return num / 2

greet_programmer()  
greet("Alice")  
greet_with_default()  
greet_with_default("Bob")  
print(add(2, 3))  
print(halve(10))  
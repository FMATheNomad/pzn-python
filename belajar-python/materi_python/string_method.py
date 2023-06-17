string = "hello world"
print(string.capitalize())
# Output: "Hello world"
string = "Hello World"
print(string.lower())
# Output: "hello world"
string = "Hello World"
print(string.upper())
# Output: "HELLO WORLD"
string = "  Hello World  "
print(string.strip())
# Output: "Hello World"
string = "Hello,World,Python"
print(string.split(","))
# Output: ["Hello", "World", "Python"]
list = ["Hello", "World", "Python"]
print(",".join(list))
# Output: "Hello,World,Python"
string = "Hello World"
print(string.replace("World", "Python"))
# Output: "Hello Python"
string = "Hello World"
print(string.startswith("Hello"))
# Output: True
string = "Hello World"
print(string.endswith("World"))
# Output: True

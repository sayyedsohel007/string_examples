# User se string input lena
s = input("Enter a string: ")

# Unique characters store karne ke liye empty string
result = ""

# Har character check karna
for ch in s:
    # Agar character pehle se result me nahi hai
    if ch not in result: # Agar character pehle se result me nahi hai to usko result me add karte hai
        result += ch

# Duplicate-free string print karna
print(result)
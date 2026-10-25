# punctuation characters use karne ke liye string module import karna
import string

# User se string input lena
s = input("Enter a string: ")

# Result store karne ke liye empty string
result = ""

# Har character check karna
for ch in s:
    # Agar character punctuation nahi hai
    if ch not in string.punctuation:  #string.punctuation ka use karke check karte hai ki character punctuation hai ya nahi
        result += ch

# Final string print karna
print(result)
# User se string input lena
s = input("Enter a string: ")

# Digits store karne ke liye empty string
digits = ""

# Har character check karna
for ch in s:
    # Agar character digit hai
    if ch.isdigit(): #isdigit() method ka use karke check karte hai ki character digit hai ya nahi
        digits += ch

# Digits print karna
print("Digits:", digits)
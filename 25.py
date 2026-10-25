# User se string input lena
s = input("Enter a string: ")

# Alphabets store karne ke liye empty string
alphabets = ""

# Har character check karna
for ch in s:
    # Agar character alphabet hai
    if ch.isalpha(): #isalpha() method ka use karke check karte hai ki character alphabet hai ya nahi
        alphabets += ch

# Alphabets print karna
print("Alphabets:", alphabets)
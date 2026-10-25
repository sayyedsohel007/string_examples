
# User se string input lena
s = input("Enter a string: ")

# Uppercase count ke liye variable
upper_count = 0

# Lowercase count ke liye variable
lower_count = 0

# Har character check karna
for ch in s:
    # Agar character uppercase hai
    if ch.isupper():  #isupper() method ka use karke check karte hai ki character uppercase hai ya nahi
        upper_count += 1
    # Agar character lowercase hai
    elif ch.islower(): # islower() method ka use karke check karte hai ki character lowercase hai ya nahi
        lower_count += 1

# Dono counts print karna
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
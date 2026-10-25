# User se string input lena
s = input("Enter a string: ")

# Vowels ki list banana
vowels = "aeiouAEIOU"

# Vowels count store karne ke liye variable
count = 0

# String ke har character ko check karna
for ch in s:
    # Agar character vowel hai
    if ch in vowels:
        count += 1

# Total vowels print karna
print("Vowels:", count)
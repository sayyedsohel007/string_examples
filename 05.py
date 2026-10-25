# User se string input lena
s = input("Enter a string: ")

# Vowels ki list banana
vowels = "aeiouAEIOU"

# Consonants count store karne ke liye variable
count = 0

# String ke har character ko check karna
for ch in s:
    # Agar character alphabet hai aur vowel nahi hai
    if ch.isalpha() and ch not in vowels:
        count += 1

# Total consonants print karna
print("Consonants:", count)
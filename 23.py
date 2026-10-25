# User se string input lena
s = input("Enter a string: ")

# String ko lowercase karna aur spaces hatana
s = s.lower().replace(" ", "") #lower() method ka use karke string ko lowercase karte hai aur replace() method ka use karke spaces hatate hai
# Original aur reverse string compare karna
if s == s[::-1]:  #[::-1] slicing se string reverse karte hai
    print("String is a palindrome")  
else:
    print("String is not a palindrome")
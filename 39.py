# User se string input lena
s = input("Enter a string: ")

# isidentifier() se valid identifier check karna
if s.isidentifier(): # isidentifier() method ka use karke check karte hai ki string valid identifier hai ya nahi
    print("Valid identifier")
else:
    print("Not a valid identifier") 
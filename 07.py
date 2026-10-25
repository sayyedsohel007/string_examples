# User se string input lena
s = input("Enter a string: ")

# User se substring input lena
sub = input("Enter substring: ")

# endswith() se check karna
if s.endswith(sub): #endswith() method ka use karke check karte hai ki string sub se end hoti hai ya nahi
    print("Yes, string ends with", sub)
else:
    print("No, string does not end with", sub)
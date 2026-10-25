# User se string input lena
s = input("Enter a string: ")

# User se substring input lena
sub = input("Enter substring: ")

# startswith() se check karna
if s.startswith(sub):  #satrtswith() method ka use karke check karte hai ki string sub se start hoti hai ya nahi
    print("Yes, string starts with", sub)  
else:
    print("No, string does not start with", sub)
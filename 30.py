# User se string input lena
s = input("Enter a string: ")

# istitle() se title case check karna
if s.istitle():  #istitle() method ka use karke check karte hai ki string title case hai ya nahi
    print("String is in title case")
else:
    print("String is not in title case")
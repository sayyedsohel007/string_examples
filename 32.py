# User se string input lena
s = input("Enter a string: ")

# islower() se check karna
if s.islower():  #islower() method ka use karke check karte hai ki string me saare characters lowercase hai ya nahi
    print("All characters are lowercase")
else:
    print("All characters are not lowercase")
# User se string input lena
s = input("Enter a string: ")

# isalpha() se check karna
if s.isalpha():  #isalpha() method ka use karke check karte hai ki string me sirf alphabets hain ya nahi
    print("String contains only alphabets")
else:
    print("String does not contain only alphabets")
# User se string input lena
s = input("Enter a string: ")

# User se character input lena
ch = input("Enter character: ")

# find() se character ka index nikalna
index = s.find(ch) #find() method ka use karke check karte hai ki string me character ch ka index kya hai. Agar character nahi milta to -1 return hota hai

# Agar character mila hai
if index != -1:
    print("Index:", index)
else:
    print("Character not found")
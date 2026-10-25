# User se string input lena
s = input("Enter a string: ")

# User se character input lena
ch = input("Enter character: ")

# find() se first occurrence nikalna
first = s.find(ch)

# rfind() se last occurrence nikalna
last = s.rfind(ch)  #rfind() method ka use karke check karte hai ki string me character ch ka last occurrence kya hai. Agar character nahi milta to -1 return hota hai

# Dono index print karna
print("First occurrence:", first)
print("Last occurrence:", last)
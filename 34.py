# User se string input lena
s = input("Enter a string: ")

# Har character ka ASCII value nikalna
for ch in s:
    # ord() function ASCII value deta hai
    print(ch, "=", ord(ch))  #ord() function ka use karke check karte hai ki character ka ASCII value kya hai
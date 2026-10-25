# User se sentence input lena
sentence = input("Enter a sentence: ")

# User se word input lena
word = input("Enter a word: ")

# Word ko sentence ke words me check karna
if word in sentence.split(): #split() method ka use karke sentence ko words me divide karte hai
    print("Word exists in sentence")
else:
    print("Word does not exist in sentence")
# User se sentence input lena
sentence = input("Enter a sentence: ")

# split() se words ki list banana
words = sentence.split()  #split() method ka use karke sentence ko words me divide karte hai

# Words ki total count print karna
print("Number of words:", len(words))
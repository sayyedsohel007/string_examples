# User se sentence input lena
sentence = input("Enter a sentence: ")

# Sentence ko words me split karna
words = sentence.split()  #split() method ka use karke sentence ko words me divide karte hai

# Pehle word ko shortest maan lena
shortest = words[0]

# Har word check karna
for word in words:
    # Agar current word shortest se chhota hai
    if len(word) < len(shortest):  # Agar current word shortest se chhota hai to usko shortest me update karte hai
        shortest = word

# Shortest word print karna
print("Shortest word:", shortest)
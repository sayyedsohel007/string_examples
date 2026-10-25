# User se sentence input lena
sentence = input("Enter a sentence: ")

# Sentence ko words me split karna
words = sentence.split()  #split() method ka use karke sentence ko words me divide karte hai

# Pehle word ko longest maan lena
longest = words[0]

# Har word check karna
for word in words:
    # Agar current word longest se bada hai
    if len(word) > len(longest): # Agar current word longest se bada hai to usko longest me update karte hai
        longest = word

# Longest word print karna
print("Longest word:", longest)
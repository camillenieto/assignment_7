# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

sentence = input("Enter a sentence : ")
vowels = 0
consonants = 0
special_character = 0

print(sentence)
no_of_words = len(sentence.split())
#i used split() to count words in the sentence

print("The number of words are : " + str(no_of_words))


for i in sentence:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or
       i=='A' or i=='E' or i=='I' or i=='O' or i=='U') :
       vowels = vowels+1
    else:
        consonants = consonants+1

print("The number of vowels are : ",vowels)
print("The number of consonants are : ",consonants - sentence.count(" "))

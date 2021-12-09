# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

import string

while True :

    password = input("Enter Password: ")
    uppercase_letters = 0
    numbers = 0
    special_char = 0
    
    for i in password :
         if i in string.ascii_uppercase :
             uppercase_letters += 1
         if i in string.digits :
             numbers += 1
         if i in string.punctuation :
             special_char += 1
    
    if not len(password) > 15:
        print("Password must be more than 15 characters")
    if not uppercase_letters:
        print("Password should at least one uppercase letter")
    elif not numbers:
        print("Password should have at least one number")
    elif not special_char:
        print("Password should have at least one special character")
    else:
        print("Your password is valid")
        break

    print(password)
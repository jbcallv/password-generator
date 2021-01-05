# Password generator
""" 
    -user inputs the length of the password he/she wishes to create
    -user can (optional) input characters that should be present in the password
    -password is generated and printed to console
"""

# import necessary modules
import random

generation_text = "abcdefABCDEF1234567890!@#$%^&*()/"

def generate(length, special_chars):
    """ generates a password 

    :param length: length of password to be generated
    :param special_chars: special characters to include
    :rtype: string containing generated password
    """
    iter_times = length - len(special_chars)
    return_string = ""

    for i in range(iter_times):
        return_string += generation_text[random.randint(0, len(generation_text)-1)]
    
    for letter in special_chars:
        return_string = insertChar(return_string, letter, random.randint(1, len(return_string)))

    return return_string

def insertChar(string, char, index):
    """ inserts a character to the string
    
    :param string: the string on which to perform the insertion
    :param index: the index at which to insert
    """
    return string[:index] + str(char) + string[index:]

# driver code
if __name__ == "__main__":
    pwd_length = int(input("Please enter the length of the password you wish to generate: "))
    print()
    print("Leave the following blank if you do not wish to input special characters.")
    pwd_chars = str(input("Please enter some characters you'd like to use: "))
    print()
    print("Generating password")
    print()
    print("Your new password is:")
    print(generate(pwd_length, pwd_chars))
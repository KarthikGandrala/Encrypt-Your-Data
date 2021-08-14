#!/usr/bin/python
# -*- coding: utf-8 -*-

# Function to rotate each letter with the specified key

def reverseBasicRotate(letter, key):
    
    # Checks if letter is lowercase

    if letter.islower():
        
        # As long as letter is lowercase, key is added
                
        new = ord(letter) + key
        
        # If letter has gone past z, 26 is subtracted to even it out

        if new > ord('z'):
            new = new - 26
        if new < ord('a'):
            
        # If letter has gone past a, 26 is subtracted to even it out
            
            new = new + 26
            
        new = chr(new)
    else:
        
         # Else condition is defined to encrypt Upper case letters

        new = letter
        
        # Checks If letter is upper case, than key is added

        if letter.isupper():
            new = ord(letter) + key
                        
            # If letter has gone past capital Z, 26 is subtracted to even it out

            if new > ord('Z'):
                new = new - 26
            
            # If letter has gone past capital A, 26 is subtracted to even it out

            if new < ord('A'):
                new = new + 26
            new = chr(new)
        else:
            
            # If none of these conditions are satsifed, the letter is returned as is

            new = letter

    return new


def encrypt(message, key):
    
    # Empty list defined to store the encrypted values

    encrypted = ''
    for character in message:
        
        # For loop is run to the length of the message.

        encrypted += reverseBasicRotate(character, key)
        
    # Encrypted string is returned

    return encrypted

# Decrypt function utilised a reverse encrypt function

def decrypt(message, key):
    return encrypt(message, -key)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:03:54 2025

@author: nicholascullen
"""

passwords = ["123456", "123456789", "12345", "qwerty", "password", "12345678", "111111", "123123", "1234567890", "1234567", "qwerty123", "000000", "1q2w3e", "aa12345678", "abc123", "password1", "1234", "qwertyuiop", "123321", "password123", "1q2w3e4r5t", "iloveyou", "654321", "666666", "987654321", "123", "123456a", "qwe123", "1q2w3e4r", "7777777", "1qaz2wsx", "123qwe", "zxcvbnm", "121212", "asdasd", "a123456", "555555", "dragon", "112233", "123123123", "monkey", "11111111", "qazwsx", "159753", "asdfghjkl", "222222", "1234qwer", "qwerty1", "123654", "123abc"] ## list of common passwords
strongPasswords = [] ## list of strong passwords
userPreference = True ## control for if the user wants to use app again

def getPassword(): ## function to get user input for password
    userPassword = input(str("What would you like your password to be? ")) ## line to get user input for password

    return (userPassword) ## returns user input password

def check(password): ## function to check user input for password against list of common passwords
    checkIndex = 0 ## index of common password element
    
    while checkIndex < len(passwords): ## iterates through common password list
        if password == passwords[checkIndex]: ## checks if passed parameter for password is within the common paswords list
            print("Your password is too common. It was found at index ", checkIndex,". Please consider changing it.") ## notifies user that the input password was in the common passwords list
            return (False) ## returns that the user input password was found in the common passwords list
            break ## breaks out of loop if user input password was in the common passwords list
        checkIndex = checkIndex + 1 ## increments the index for the loop control
    
    return (True) ## returns that the user input password was not found in the common passwords list
        
def validate(password): ## function to validate that the user input password has the correct elements
    length = False ## boolean for if the length is valid
    upper = False ## boolean for if an uppercase character is detected
    lower = False ## boolean for if a lowercase character is detected
    digit = False ## boolean for if a digit character is detected
    special = False ## boolean for if a special character is detected
    specialChars = ["#","$","-","_","+","+"] ## list of valid special characters
    passwordElements = list(password) ## converts password into a list of individual characters
    
    if((len(password) >= 8)): ## checks if length of password is valid
        length = True ## updates length boolean
    
    for char in passwordElements: ## loop to check what each password element is
        if char.isupper(): ## checks if upper case character is detected 
            upper = True ## updates uppercase boolean
        elif char.islower(): ## checks if lower case character is detected 
            lower = True ## updates lowercase boolean
        elif char.isdigit(): ## checks if digit is detected
            digit = True ## updates digit boolean
        elif char in specialChars: ## checks if special character is detected
            special = True ## uopdates special character boolean 
            
    if (length and upper and lower and digit and special): ## checks if all booleans are true
        return True ## returns true if password is valid
    else: 
        return False ## returns false if password is invalid
    
def main(): ## function to run program
    finalCheck = False ## boolean for if all parameters are valid for password
    valid = False ## boolean for if the password is strong enough
    checkValid = False ## boolean for if the password is contained in the common passwords list
    
    username = input(str("What would you like your username to be? ")) ## asks user for the username they would like to use
    
    while (finalCheck == False): ## loop to ensure password is valid
        userPassword = getPassword() ## asks user for password and stores in a variable
        if (checkValid == False): ## checks if user input is in the common passwords list
            checkValid = check(userPassword) ## calls function to check
        if (checkValid == True): ## checks if user input was not in common passwords list
            valid = validate(userPassword) ## validates if password is strong enough
        if(valid): ## checks that the validity of the user input password
            strongPasswords.append(userPassword) ## appends user input password to a list of strong passwords
            print("You have a strong password.") ## tells user their password was valid
            finalCheck = True ## updates control varible for the loop to end it
        elif valid == False: ## checks the validity if the user input password
            print("Your password needs to be stronger. Please input another.") ## notifies user that they need a stronger password
    
    print("Your username is:", username) ## prints username
    print("Your password is:", userPassword) ## prints password

while(userPreference): ## checks if user would like to use the program again
    main() ## calls main to run the program
    useAgain = input(str("Would you like to make another username and password? Please type 'Yes' or 'No'. ")) ## asks user if they would like to use program again
    if (useAgain == "No"): ## checks user input for if they want to use again
        userPreference = False ## updates boolean for loop control variable
        
print("Thank you for using the Password Validation App") ## thanks user for using application
        
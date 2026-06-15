#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:17:11 2025

@author: nicholascullen
"""

def openFile():
    with open('/Users/nicholascullen/Desktop/FunWithFiles.txt', 'r') as file: #opens file in read mode
        movies = file.readlines() #reads each line into list
        if not movies: #checks if a file is found
            print("File not found") #prints feedback if file is not found
        else:
            movies = [line.strip() for line in movies] #turns movies into workable list
            return movies #returns movies list from function

def view():
    newList = openFile() #sets new list to the return list of openFile
    print(newList) #prints movies in the list

def add(movie):
    with open('/Users/nicholascullen/Desktop/FunWithFiles.txt', 'a') as file: #opens file in append mode
        file.write("\n" + movie) #adds movie to list

def delete(movie):
    with open('/Users/nicholascullen/Desktop/FunWithFiles.txt', 'r') as file: #opens file in read mode
        lines = file.readlines() #reads each line into list
    updatedLines = [] #list for updated lines
    for line in lines: #iterates through list to find line that needs to be replaced
        updatedLine = line.replace(movie, '') #replaces movie user wants to replace
        if updatedLine.strip(): #checks if line is not empty
            updatedLines.append(updatedLine.strip() + '\n') #appends the updated line to the list
    with open('/Users/nicholascullen/Desktop/FunWithFiles.txt', 'w') as file: #opens file in write mode
        file.writelines(updatedLines) #writes the updated list to the file
    
def main():
    while(True): #loop control for main
        action = str(input("Welcome to the menu what would you like to do? (Type: View, Add, Delete, or Exit) ")) #asks user for menu input
        if(action == "Exit"): #checks if exit was input
            break #breaks out of loop
        elif(action == "View"): #checks if action was input
            view() #calls view function
        elif(action == "Add"): #checks if add was input
            movie = str(input("Which movie would you like to add? ")) #asks user for add input
            add(movie) #calls add function
        elif(action == "Delete"): #checks if delete was input
            movie = str(input("Which movie would you like to delete? ")) #asks user for delete input
            delete(movie) #calls delete function
        else:
            print("Please type View, Add, Delete, or Exit when prompted)") #asks user to correctly use menu
    print("Thank you for using the movie app.") #thanks user for using service
    
openFile() #initially opens file
main() #calls main
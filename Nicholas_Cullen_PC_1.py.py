#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:49:17 2025

@author: nicholascullen
"""

name = input("What is your name? ")
print("Hello",name,"welcome to the Python Pizza Paradise!")

menu = ["Veggie Delight", "BBQ Chicken", "Hawaiian"]
order = []
more = "yes"
count = 0

print("We have the following pizzas", menu[0], menu[1], menu[2])
while(more == "yes"):
    type = str(input("What kind of pizza would you like? "))
    if (type == menu[0] or type == menu[1] or type == menu[2]):
        count = count + 1
        order.append(type)
        while(more !='no'):
            more = input("Would you like to order an additional pizza? ")
            if(more == 'yes'):
                break
            else:
                print("Please answer with 'yes' or 'no' only.")
    else:
        print("Sorry, we only offer Veggie Delight, BBQ Chicken, or Hawaiian. Please choose again")
print("Thank you", name,". You have ordered", count, "pizzas. Your order will be ready in 20 minutes")
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Lab for Module 5 The Bottle Return Program
# Shaheer Harris
# Code calculates total number of bottles turned in, and the payout.

# Step 1: Declare variables below 
total_bottles = 0
today_bottles = 0
counter = 0
total_payout = 0
keep_going = 'y'

# Input loop
while keep_going == 'y':
    total_bottles = 0
    #Loop for each day of the week
    for day in range(1, 8):
        today_bottles = int(input(f'Enter number of bottles for day #{day}: '))  # Get input for bottles collected today
        total_bottles += today_bottles
    total_payout = total_bottles * 0.1  # Calculate total payout

    # Printing totals
    print('\nThe total number of bottles collected is', total_bottles)
    print('The total paid out is $ {:.1f}\n'.format(total_payout))

    # Loop condition
    keep_going = input("Do you want to enter another week's worth of data? Enter y or n: ").lower() 
    print()  


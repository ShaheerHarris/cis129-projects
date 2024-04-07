#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Module 4 Lab-4
# Shaheer Harris
# 04/06/24
# Code will determine monthly costs

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase

# Prompt for monthly sales amount
prompt = "Enter monthly sales amount: "

# Calculate monthly sales and percent of sales increase
monthlySales = float(input(prompt))
salesIncrease = float(input("Enter the percent of sales increase: "))

# Calculate store bonus amount
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# Calculate employee bonus amount
if salesIncrease >= 0.05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if storeAmount == 6000 and empAmount == 75:
    print('Congrats! You have reached the highest bonus amounts possible!')


# In[ ]:





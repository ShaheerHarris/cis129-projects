#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

# Checking if file exists
if not os.path.exists("grades.txt"):
    # Creating file if not
    print("File doesn't exist. Creating 'grades.txt'.")
    file = open("grades.txt", 'w')
else:
    # If the file exists, open it
    print("File exists. Opening 'grades.txt'.")
    file = open("grades.txt", 'a')

print('Enter any number of grades (-1 to quit)')

# Inputing the grades
while True:
    grade = int(input())
    if grade == -1:
        break
    else:
        file.write(f'{grade}\n')

file.close()


# In[ ]:





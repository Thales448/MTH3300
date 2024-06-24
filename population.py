#******************************************************************************
# population.py
#******************************************************************************
# Name: Rodrigo Valenzuela
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#NONE
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
"""
Population Homework: Calculate the population growth given changing intervals of time and growth rate. 
Cumulatively using only three variables
"""
import math

print("Welcome to the Population Calculator\n Start by inputing your initial Population")
P = int(input("Population:"))
rtsums = 0
for num in range(3):
    place = ['first', 'second', 'third'] 
    rtsums +=(float(input(f"Enter {place[num]} time period (in years): "))* (float(input(f'Enter {place[num]} growth rate (in percentage): '))/100))
print(f'The final population is {P*math.exp(rtsums)}')
#nevermind
    

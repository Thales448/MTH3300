#******************************************************************************
# sprinkler.py
#******************************************************************************
# Name: Rodrigo Valenzuela
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#NONE
#Time: 
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#output needs, total squarefeet, irrigated squarefeet (80%), sprinklers needed (3.11 Gpm)
# total gallons per minute + cost 
"""
Enter width (in ft): 30
Enter length (in ft): 40
You have 1200.0 square feet of yard area and 960.0 square feet for irrigation.
You will need 7 sprinklers in your yard.
It will use about 21.77 gallons per minute when running.
Your bill will bE about $58.81 per month.

one sprinkler = 155 ft^2 @ 3.11Gpm @ $4.49 per 1000 ft^3 15 min a day

"""
import math
# User inputs:
width =  input("Enter width (in ft):")
length =  input(" Enter length (in ft):")

#Needed calculations
area = float(width) * float (length) #thought of using int in the input function but might loose data to early in my calculations
irrigated_area = (area * .8) # inintaliy i rounded this value but it wasnt passing tests WHO says 379.20000000000005 square feet??

#calculating sprinklers needed so we get 100% coverage no matter what ( initially thought of int() + 1 but that wouldnt work in perfect divisions by 155
if irrigated_area % 155 == 0:
  sprinklers_needed = irrigated_area / 155
else:
  sprinklers_needed = int(irrigated_area/155) + 1

water_use_per_minute = round((sprinklers_needed * 3.11), 2) 
bill = round(((water_use_per_minute * 15 * 30) / 748 * 4.49), 2)

# creating printed output 
print(f' You have {area} square feet of yard area and {irrigated_area} square feet for irrigation.\nYou will need {sprinklers_needed} sprinklers in your yard.\nIt will use about {water_use_per_minute} gallons per minute when running.\nYour bill will be about ${bill:.2f} per month.')
# your code has as an output 'bE' i didi it exactly and the autograder didint like that

# Step 1
# In this workshop, you will practice working with numbers and mathematical operations to build a bill splitter.
# This tool will calculate how much each person owes after adding meal costs and a tip.
# To start, you need a way to keep track of the total amount as costs are added.
# In Python, you can use a variable to store an integer (a whole number) that changes over time.
# For example:
# my_number = 2
# Create a variable named running_total and assign it the value 0.

# Step 2
# Next, you need to account for the number of people sharing the bill.
# Store this value in a variable, as you did in the previous step.
# Create a variable named num_of_friends and assign it the value of 4.
# This will be used later in the workshop to calculate the final split.

# Step 3
# Each course has a cost. You need to store these amounts in variables to use them later.
# Since these amounts include cents, you will use the float type.
# Example:
# change = 2.35
# Create four variables:
# appetizers = 37.89
# main_courses = 57.34
# desserts = 39.39
# drinks = 64.21

# Step 4
# Now that you have stored the individual costs, you can calculate the total.
# Use the += operator to add appetizers, main_courses, desserts, and drinks to running_total.
# Finally, print the total bill so far.

# Step 5
# Calculate a 25% tip by multiplying running_total by 0.25.
# Store it in a variable named tip.
# Print the tip amount.

# Step 6
# Add the tip to running_total using +=
# Print the total with tip.

# Step 7
# Divide the running_total by num_of_friends to find how much each person pays.
# Store it in final_bill.
# Print the bill per person.

# Step 8
# Round final_bill to 2 decimal places using round().
# Store it in each_pays.
# Print "Each person pays:" along with the value.

# --------- ACTUAL CODE ---------

running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)
# User input
apples = int(input("Please enter a number of apples in a basket: "))
people_num = int(input("Please enter a number of children: "))

# Variables calculation
apples_to_each = apples // people_num
remaining_apples = apples % people_num

# Two separate print statements for better code readability
print(f'Each child gets {apples_to_each} apples.')
print(f'Number of the apples remaining in the basket is {remaining_apples}')

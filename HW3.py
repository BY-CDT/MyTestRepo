# User input
class_1 = int(input("Please enter a number of children for class 1: "))
class_2 = int(input("Please enter a number of children for class 2: "))
class_3 = int(input("Please enter a number of children for class 3: "))

# Desks calculation
desk_count_1 = (class_1 // 2) + (class_1 % 2)
desk_count_2 = (class_2 // 2) + (class_2 % 2)
desk_count_3 = (class_3 // 2) + (class_3 % 2)

# Result Output
desk_count_total = desk_count_1 + desk_count_2 + desk_count_3
print(f'Total of {desk_count_total} desks is needed.')

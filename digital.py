# Read the month integer from input
m = int(input())

# List of days in each month for the year 2019
# Index 0 is a placeholder so that index 1 = January, 2 = February, etc.
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Output the number of days for the given month m
print(days_in_month[m])

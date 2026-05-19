# Read the number of articles and target impact factor from a single line of input
a, i = map(int, input().split())

# Apply the formula to find the minimum citations required
# Since rounding is always up, we need the citations to be 
# just enough to exceed the previous integer (I-1).
minimum_citations = a * (i - 1) + 1

# Output the result
print(minimum_citations)

import sys

# Read input from stdin, split into two strings
a, b = sys.stdin.read().split()

# Reverse the strings using slicing [::-1]
rev_a = int(a[::-1])
rev_b = int(b[::-1])

# Output the larger of the two reversed numbers
print(max(rev_a, rev_b))
import sys

# Read the input from standard input
for line in sys.stdin:
    n = float(line.strip())
    # Round to the nearest integer and print
    print(round(n))

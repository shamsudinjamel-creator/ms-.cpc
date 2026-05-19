# Read input
x1, y1 = map(int, input().split())  # Petra's rook
x2, y2 = map(int, input().split())  # Garðar's pawn

# Check conditions
if x1 == x2 or y1 == y2:
    print(1)
else:
    print(2)
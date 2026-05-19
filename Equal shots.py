import sys

def main():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse the number of ingredients for both shots
    a = int(input_data[0])
    b = int(input_data[1])
    
    idx = 2
    
    # Calculate total alcohol units and total volume for the first shot
    total_alcohol_1 = 0
    total_volume_1 = 0
    for _ in range(a):
        v = int(input_data[idx])
        c = int(input_data[idx+1])
        total_alcohol_1 += v * c
        total_volume_1 += v
        idx += 2
        
    # Calculate total alcohol units and total volume for the second shot
    total_alcohol_2 = 0
    total_volume_2 = 0
    for _ in range(b):
        v = int(input_data[idx])
        c = int(input_data[idx+1])
        total_alcohol_2 += v * c
        total_volume_2 += v
        idx += 2

    # Cross-multiply to check if the alcohol percentages (by volume) are equal:
    # (total_alcohol_1 / total_volume_1) == (total_alcohol_2 / total_volume_2)
    if total_alcohol_1 * total_volume_2 == total_alcohol_2 * total_volume_1:
        print("same")
    else:
        print("different")

if __name__ == "__main__":
    main()
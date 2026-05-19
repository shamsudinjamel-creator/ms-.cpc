Kattis logo
Kattis

Problems
Contests
Challenge
Ranklists
Jobs (5)
Languages
Info
Help
Kattis Cat
Search Kattis
Submission 19723588
Support Kattis
Shamsudin Jamel
Submission 19723588
Edit and resubmit
Date	Problem	Judgement	Runtime	Language	Test cases
21:49:53	Equal Shots	
Accepted
0.04 s	Python 3	
28/28
Files submitted
Mainfile: equalshots.py
equalshots.py
 Download equalshots.py
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

Contact System Status Terms of Service Privacy Policy

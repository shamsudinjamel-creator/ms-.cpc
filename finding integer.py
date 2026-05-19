import sys

def solve():
    # Read the input string from standard input
    s = sys.stdin.read().strip()
    
    # Find the index of the first occurrence of 'a'
    index = s.find('a')
    
    # Print the suffix starting from that index
    print(s[index:])

if __name__ == "__main__":
    solve()
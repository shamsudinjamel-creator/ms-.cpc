import sys

def solve():
    # Read the input DNA string from standard input
    dna_string = sys.stdin.read().strip()
    
    # Check if 'COV' is a substring of the input
    if "COV" in dna_string:
        print("Veikur!")  # Meaning 'Sick!' in Icelandic
    else:
        print("Ekki veikur!") # Meaning 'Not sick!' in Icelandic

if __name__ == "__main__":
    solve()

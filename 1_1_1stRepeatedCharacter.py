# An efficient solution is to use Hashing to solve this in O(n) time on average.

# Create an empty hash.
# Scan each character of input string and insert values to each keys in the hash.
# When any character appears more than once, hash key value is increment by 1, and return the character.

# Python program to find the first
# repeated character in a string
def firstRepeatedChar(str):
 
    h = {}  # Create empty hash
 
    # Traverse each characters in string
    # in lower case order
    for ch in str:
 
        # If character is already present
        # in hash, return char
        if ch in h:
            return ch;
 
        # Add ch to hash
        else:
            h[ch] = 0
 
    return
 
 
# Driver code
print(firstRepeatedChar("gekfors"))
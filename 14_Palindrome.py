#given a string, check if it is a permutation of a palindrome.
#input = tact coa
#output = True

#if you rearrange the letters, is the string the same forwards and backwards?

#check to see if without rearranging that it is a palindrome:
def isPalendrome(s1):
    word = {} #empty hash
    oddCount = 0
    str = ""
    for i in s1:
        str = i + str
    if str == s1:
        return (s1 +'is a palindrome');
    # return False;
    # we know its nots the same in reverse, so now we need permutations.
    for ch in s1:
        if ch in word:
            word[ch]=word[ch]+1
 
        # Add ch to hash
        else:
            word[ch] = 1
    #at most, only one char can have an odd count.
    for key in word:
        if word[key] % 2 > 0:
            print (key+ 'appears odd')
            oddCount = oddCount+1;
    if oddCount > 1:
        print (s1 + 'is not a palindrome');
    else: print (s1 + 'is a palindrom');
    return word;
    



# print(isPalendrome('glen'))
# print(isPalendrome('mom'))
print(isPalendrome('tactcoa'))
print(isPalendrome('glenelgn'))
print(isPalendrome('glen'))
print(isPalendrome('wow'))



# Given 2 strings, write a method to decide of one is a permutation of the other
# They should contain the same characters

def isItPerm(s1, s2):
    isPerm = True;
    if len(s1) == len(s2):
        if s1 == s2:
            return True;
        else:
            for ch in s1:
                if not(ch in s2):
                    isPerm = False;
        return isPerm;
            

print(isItPerm('abc', 'cba'));
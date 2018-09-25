#compress a string (repeated characters compressed to char and count) to a string of chars and counts, compress.
#example: X is aaabcccccaaa, then Y is a31b5c3a
#the length of Y is less than the length of X, so recommed compression
#abc is a1b1c1, Y > X, do not recommend compression.

def compress(s1):
    # h1={}
    compressedString = ''
    consecutive = 0
    if len(s1) <= 3:
        return ('compression not recommended ' +s1)
    else:
        print ('more work needs to be done' + s1)
        #if the next char is diff, append this char to result
        for index in range(0,(len(s1))): #length of abc is 3, if index at 2 we are at the end of the string
            consecutive +=1
            if (index + 1 >= len(s1) or s1[index] != s1[index+1]): #if nothing to compare to or the next char is not the same, append char
                compressedString += s1[index]+ str(consecutive)
                consecutive = 0
                #if the 2 chars are the same (false), or we are not at the end (true for dd), consecutive not set back to 0, becomes 1 
  
    print (compressedString)
    if len(compressedString)<len(s1):
        return ('compress it')
    print len(compressedString)
    print len(s1)
    return ('don\'t compress')
        



print(compress('a'))
print(compress('ab'))
print(compress('abc'))
print(compress('abccdddcccc'))

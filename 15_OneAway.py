#onneaway
# Given 2 strings, write a function to check if they are one edit (or 0) away
# pale ple - true
# plaes, plae - True
# pale, bake - false

def isOneAway(s1,s2):
    missingCount = 0
    lenDiff = 0

    if(s1 == s2):
        return ('better than 1 away!')
    else:
        lenDiff =  len(s1) - len(s2)
        if lenDiff < -1 or lenDiff > 1:
            return ('more than one away in length')
        else:
            print('not same length')
            for ch in s1:
                if ch not in s2:
                    print (ch +' is not in '+str(s2))
                    missingCount+=1
            if missingCount == 1:  
                return ('one away')
            else:
                return ('more than one away')


# print(isOneAway('pale','pale'))
# print(isOneAway('pales','pale'))
# print(isOneAway('pale','bale'))
# print(isOneAway('pale','bake'))
# print(isOneAway('paaa','paa'))
print(isOneAway('aaale','paale'))


    # for ch in s1:
    #     if ch in h1:
    #         h1[ch] = h1[ch]+1
    #     else:
    #         h1[ch]=1
    # for ch in s2:
    #     if ch in h2:
    #         h2[ch] = h2[ch]+1
    #     else:
    #         h2[ch] = 1
    
    # print(h1)
    # print(h2)
    # for chX in h1:
    #     if chX not in h2:
    #         print (str(chX) + ' not in ' + str(h2))
    #         missingCount+=1;
    # if missingCount == 1:
    #     print ('one away by 1 character')


    # return missingCount;

def findPalindrome(str):
    h = {}
    palin = ''
    if len(str) == 1:
        return False
    else:
        for i in range (0,len(str)):
            print (str[i])
            if str[i] == str[i+1]:
                if i == 0:
                    h[str[i]+str[i+1]] = 2
                    print(2)
                else:
                    print (i,i-1,i+2,len(str))
                    j=i
                    while(j-1 >= 0 and j+2 <= len(str)):
                        print ('j is ',j)
                        print ('str',j, ' is ' ,str[j])
                        print ('str',j-1, ' is ' ,str[j-1])
                        j=j+1
                        # print ('in middle ',str[i-1],str[i+2])


                # return (str[i], 'same as ', str[i+1], ' 2 char palin')
            else:
                print(str[i], 'NOT same as ', str[i+1])
        return(h)


print (findPalindrome('dbaab'))            

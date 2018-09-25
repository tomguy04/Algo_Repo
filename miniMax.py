def miniMaxSum(arr):
    low = 0
    high = 0
    sum = 0
    lowhigh=[]

    for i in range (len(arr)):
        sum+=arr[i]
    
    low = sum- (max(arr))
    high = sum- (min(arr))

    lowhigh.append(low)
    lowhigh.append(' ')
    lowhigh.append(high)
    
    print map(str,lowhigh)


    return ''.join(map(str, lowhigh))

print miniMaxSum([1,2,3,4,5])
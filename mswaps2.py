def bribe(arr):
    moves = 0
    print 'before ',arr
    n=len(arr)
    for i in range (n-1):
        if arr[i] != i+1:
            print arr[i], ' in ', i
            print 'swap ', i, arr.index(i+1)
            print arr[i], arr[arr.index(i+1)]
           
            #find where i+1 is
            print i+1, ' is in ', arr.index(i+1)
            #swap

            original = arr[i]
            temp = arr.index(i+1)
            print 'swapping arr[i] was' ,arr[i], 'and i+1 was ',arr[arr.index(i+1)]
            arr[i]=arr[arr.index(i+1)]
            print 'arr[i] is ' ,arr[i], 'and i+1 is ',arr[arr.index(i+1)], 'arr is ', arr, 'temp is', temp, 'going to swap in pos ', temp-1
            arr[temp]=original
            # arr[i], arr[arr.index(i+1)] = arr[arr.index(i+1)],arr[i]
            print 'between ', arr
            moves+=1
    print arr

    # n = len(arr)
    # for i in range (n):
    #     for j in range(0,n-i-1):
    #         if arr[j+1] < arr[j]:
    #             print arr[j],arr[j+1]
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #             moves+=1
    #             print 'between ', arr
    # print 'after ',arr
    return(moves)

print bribe([4,3,1,2])
print bribe([2,3,4,1,5])
print bribe([1,3,5,2,4,6,8])
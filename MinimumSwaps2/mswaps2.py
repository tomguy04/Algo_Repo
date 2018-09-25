def bribe(arr):
    moves = 0
    print 'before ',arr
    n = len(arr)
    for i in range (n):
        for j in range(0,n-i-1):
            if arr[j+1] < arr[j]:
                print arr[j],arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                moves+=1
                print 'between ', arr
    print 'after ',arr
    return(moves)

print bribe([4,3,1,2])
# print bribe([2,3,4,1,5])
# print bribe([1,3,5,2,4,6,8])
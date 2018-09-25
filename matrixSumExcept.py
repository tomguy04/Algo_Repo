def sumMat (arr,x,y):
    total=0
    for row in arr:
        for i in row:
            total+=i

    total-= arr[x][y]
    return total



print (sumMat([[1,2,4],[5,6,8]],0,2))
        
# sumExcept([1, 2, 4][5, 6, 8],0,2)
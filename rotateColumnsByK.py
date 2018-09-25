def printMat(mat):
    print '----------------------'
    for row in mat:
        print row

def rotateK(mat,k):
    # get height and width
    height = len(mat) #3x3, height = 3
    width = len(mat[0]) #3
    tempArr=[]

    print 'height ', height, 'width ', width
    # copy last column to temp arr
    for row in range(height): #0-2
        tempArr.append(mat[row][width-1])
      
    print 'the temp array is ', tempArr

    sourceColumn = width-2 #far right #3 #2
    destColumn = width-1 #2nd from right #2 #1

    for row in mat:
        print row
    print '---------------------'

    while k > 0:
        print 'k ',k
        sourceColumn = width-2 #far right #3 #2
        destColumn = width-1 #2nd from right #2 #1
        while sourceColumn >=0:
            for row in range(height): #0-3
                # print row, sourceColumn, ' to ', row, destColumn
                mat[row][destColumn] = mat[row][sourceColumn] #03 13 23 33 = 02  12  22  32
            destColumn-=1
            sourceColumn-=1
        # printMat(mat)
        k-=1
        # copy last column to temp arr
        
        
        for i in range(len(tempArr)):
            mat[i][0]=tempArr[i]
        tempArr=[]
        for row in range(height): #0-2
            tempArr.append(mat[row][width-1])
    #put original far right to far left.
    

    printMat(mat)

rotateK([[1,2,3,4],[5,6,7,8],[9,10,11,12]],2)




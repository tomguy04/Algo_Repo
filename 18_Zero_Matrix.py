#in an element in an MxN matrix is 0, its entire row and column are set to 0.

myMatrix = [
    [2,2,0,3],
    [1,1,0,1],
    [2,2,0,2]
]

def printMatrix(matrix):
    for row in matrix:
        print row
    print'------------'

def zeroMatrix(matrix):
    for row in matrix:
        print row

    #height
    height = len(matrix)
    #width
    width = 0
    width = len(myMatrix[0])
    
    print ('height is '+ str(height))
    print ('width is '+ str(width))

    # for row in range(0,height):
    #     for col in range (0,width):
    #         if matrix[row][col] == 0:
    #             print row,col,matrix[row][col]
    #             print '-------------------------'
    #             for i in range(0,width):
    #                 matrix[row][i] = 0
    #         printMatrix(matrix)

    row = 0
    col = 0

    while col < width and row < height:
        if matrix[row][col] == 0:
            print row,col,matrix[row][col]
            print '-------------------------' 
            for i in range(0,width):
                matrix[row][i] = 0
            for j in range(0,height):
                matrix[j][col] = 0
            row+=1
            col=0
            print '0d out and moving onto ', row,col
        else:
            col+=1
            print 'No 0s and moving onto ', row,col
        printMatrix(matrix)

    # for row in matrix:
    #     print row

zeroMatrix(myMatrix)



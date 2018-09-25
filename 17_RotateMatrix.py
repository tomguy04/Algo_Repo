matrix =[
            [1, 1, 1, 2],
            [4, 0, 0, 2],
            [4, 0, 0, 2],
            [4, 3, 3, 3]
        ]

for row in matrix:
    print row

matrixSize =len(matrix)
print ('this is a '+ str(matrixSize) +' by ' + str(matrixSize) + ' picture') 

number = 0
row = 0
temp1 = 0
temp2 = 0

#solution 1
#copy top row to array then copy left to top, bottom to left, right to bottom, temp array (old top) to right
oldTopEdge = matrix[0]

#left edge to top
for row in range(matrixSize-1,0,-1):
    # print (row) #3,2,1
    # print (str(matrix[row][0]) +" "+ str(matrix[0][row]))
    matrix[0][row]=matrix[row][0]
for row in matrix:
    print row
#bottom edge to left
for row in range(matrixSize-1,0,-1):
    # print (row) #3,2,1
    print (str(matrixSize-1)+str(row)+str(matrixSize-1-row)+str(0)+"--->"+str(matrix[matrixSize-1][row]) +" "+ str(matrix[matrixSize-1-row][0]))
    matrix[matrixSize-1-row][0]=matrix[matrixSize-1][row]
    # matrix[0][row]=matrix[row][0]


    
for row in matrix:
    print row

# for rowIndex in matrix:
#     number = rowIndex[-1]
#     print ('looking at '+ str(number))
#     if row+1 < matrixSize:
#         temp = matrix[row+1][matrixSize-1]
#         print ('replacing '+ str(temp) +' with '+ str(number))
#         matrix[row+1][matrixSize-1] = number
#         row+=1


    



# Complete the hourglassSum function below.
def hourglassSum(arr):
    myArr=[]
    for row in range (0,4):
        for col in range (0,4):
            value = 0
            for i in range (col,col+3):
                value = value + arr[row][i] + arr[row+2][i]
            value+=arr[row+1][col+1]
            myArr.append(value)
    return max(myArr)

arr = [-9, -9, -9,  1, 1, 1 ],[0, -9, 0, 4, 3, 2],[-9, -9, -9, 1, 2, 3],[0, 0, 8, 6, 6, 0],[0, 0, 0, -2, 0, 0],[0, 0, 1, 2, 4, 0]
arr2 = [1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 9, 2, -4, -4, 0],[0, 0, 0, -2, 0, 0],[0, 0, -1, -2, -4, 0]
arr3 = [1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]



print hourglassSum(arr)
print hourglassSum(arr2)
print hourglassSum(arr3)


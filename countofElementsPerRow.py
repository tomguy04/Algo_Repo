def countPresence(mat,arr):
    h={}
    rowCount = 1
    for i in arr:
        for row in mat:
            for j in row:
                if i == j:
                    if rowCount in h:
                        h[rowCount].append(j)
                        
                    else:
                        h[rowCount]=[j]
            rowCount+=1
        rowCount=1
    for i in h:
        print i, 'matches ', len(h[i]),'->',' '.join(map(str, h[i]))
    return 'done'


print (countPresence([[1,2,3],[3,4,4],[5,6,7]],[1,2,5]))